
import contextmenuComponent from './contextmenu'
// Set initial value
const defaults={
    event:''

}

// Merge function
function merge(target) {
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

// Registration plug-in
const contextmenu = {
  install: function(Vue) {
    var contextmenuConstructor = Vue.extend(contextmenuComponent);

    Vue.prototype.$contextmenu = function(options){
        // console.log(options)
        var event =event||window.event;
        // var data = merge({},defaults,options);
        var contextmenuVm = new contextmenuConstructor({
            data(){
                return {
                    top:'-500px',
                    left:'-500px',
                    items:options,
                    isShowChildIndex:null
                };
            },
            methods:{
                removeDom:function(){
                    var menu = document.getElementById('contextMenu-box');
                    if(menu){
                        menu.parentNode.removeChild(menu)
                    }
                },
                rightClick(fn){
                    fn()// Execution event
                    this.removeDom()
                }
            }
        })
       Vue.nextTick(function(){
         // Insert loading component on the next target element
        document.body.appendChild(contextmenuVm.$mount().$el); 
        var menu = document.getElementById('contextMenu');
        var left = event.clientX + 5, /* nudge to the right, so the pointer is covering the title */
            top = event.clientY;
        if (top + menu.offsetHeight >= document.body.clientHeight) {
            top -= menu.offsetHeight;
        }
        if (left + menu.offsetWidth >= document.body.clientWidth) {
            left -= menu.offsetWidth;
        }
        menu.style.zIndex=1000001;
        menu.style.left=left+'px';
        menu.style.top=top+'px';
       })
      return contextmenuVm;
    }
  }
}
export default contextmenu;