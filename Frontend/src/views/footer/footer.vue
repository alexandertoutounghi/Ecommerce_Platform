<template>
  <div id="footer">
    <div class="ft-bg">
      <div class="w-ensure mb20">
        <div class="ft_main"></div>
        <div class="ft_txt">
          <p class="ft_contact">
            <span>Service Hours：09:00-23:00</span>
            <span class="ft_phone">
              Customer Service Hotline:
              <em>010-88888888</em>
            </span>
          </p>
        </div>
      </div>
    </div>
  </div>
</template>
<script>
</script>
<style scoped  lang='scss'>
html {
  background: #fafafa;
  color: #333;
  _background-attachment: fixed;
}
html.isPhone {
  min-width: 1196px;
}
body,
p,
ul,
li {
  margin: 0;
  padding: 0;
}
body {
  font: 12px/1.5 "Microsoft YaHei", Tahoma, Helvetica, Arial, simsun;
}
i {
  font-style: normal;
}
ul {
  list-style: none;
}
img {
  border: 0;
}
a {
  text-decoration: none;
  color: #333;
  -webkit-transition: color 0.2s;
  -moz-transition: color 0.2s;
  -o-transition: color 0.2s;
  -ms-transition: color 0.2s;
  transition: color 0.2s;
}
a:hover {
  color: #2462ff;
}
a:focus,
area:focus {
  outline: 0;
}

#footer {
  border-top: 1px solid #eee;
  background: #fff;
}
#footer .ft_main {
  width: 1196px;
  margin: 0 auto;
}
#footer .ft_cata {
  display: none;
}

#footer .w-main {
  margin: 0 auto;
  width: 1200px;
}
#footer .w-main::after {
  clear: both;
  content: "";
  display: table;
}

#footer .ft_nav {
  height: 22px;
  padding: 20px 0 15px;
  text-align: center;
}
#footer .ft_nav a {
  display: inline-block;
  padding: 0 20px 0 21px;
  /*background:url(../../../static/images/footer/border-right.png) no-repeat 0 center*/
}
#footer .ft_nav a.noborder {
  background: 0;
}

#footer .ft_txt {
  text-align: center;
  padding: 8px 0;
}
#footer .ft_txt p {
  padding: 5px 0;
}
#footer .ft_txt .ft_phone {
  font-size: 14px;
}
#footer .ft_txt .ft_phone em {
  color: #6b92f7;
  font-weight: bold;
  font-size: 20px;
}
#footer .ft_txt .ft_contact span {
  display: inline-block;
  padding: 0 20px;
}
</style>
