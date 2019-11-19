import LoadingComponent from './loading.vue'
// Initialize values
const defaults={
	target:"",
	text:"",
	flag:true,
}
function merag(target) {
  for (let i = 1, j = arguments.length; i < j; i++) {
    let source = arguments[i] || {};
    for (let prop in source) {
      if (source.hasOwnProperty(prop)) {
        let value = source[prop];
        if (value !== undefined) {
          target[prop] = value;
        }
      }
    }
  }
  return target;
};
const loading = {
  install: function(Vue) {
    var LoadingConstructor = Vue.extend(LoadingComponent);
    Vue.prototype.$addLoading = function(options){
    	console.log(options);

    	var data = merag({},defaults,options);
    	var loadings = new LoadingConstructor({
    		data(){
    			return data;
    		},
    		methods:{
    			close(){
    				this.flag = false
    			}
    		}
    	})
      Vue.nextTick(function(){
        // Determine if loading is added to the target element, or if we need to remove it
        var target = document.querySelector(data.target);
        console.log(target);
        var loadingDom = target.getElementsByClassName("pio-loading2");
        if(loadingDom.length>0){
          target.removeChild(loadingDom[0]);
        }
        // Insert the loading component onto the target element
        document.querySelector(data.target).appendChild(loadings.$mount().$el); 
      })

      return loadings;
    }
  }
}
export default loading;