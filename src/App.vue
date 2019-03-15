<template>
  <div id="app">
    <div class="fiex">
      <div class="head">
          <div class="logo"><img src="./assets/bxtlogo.png"></div>
          <div class="menu">
            <ul>
              <li>
                <router-link to="/"><i class="iconfont icon-icon_square"/><div>关于倍鑫特</div></router-link>
              </li>
              <li>
                <router-link to="/productCentre"><i class="iconfont icon-icon_work"/><div>产品中心</div></router-link>
              </li>
              <li>
                <router-link to="/recruit"><i class="iconfont icon-icon_meeting"/><div>人才招聘</div></router-link>
              </li>
              <li>
                <router-link to="/"><i class="iconfont icon-icon_message"/><div>联系我们</div></router-link>
              </li>
            </ul>
          </div>

      </div>
    </div>
    <div class="body">
      <router-view/>
    </div>
    <div class="foot">

      <div class="foot-log">
        <img src="./assets/bxtlogo.png">
        <div>快速询价：18724164506</div>
        <div>地址：淮安市经济技术开发区<br>枚皋路19号智慧谷B2号楼109室</div>
      </div>

      <div class="item">
        <h3><a href="acting_brand.aspx">产品中心</a></h3>
        <ul>
          <li><a href="acting_brand.aspx?cid=1">代理品牌</a></li>
          <li><a href="advantage_brand.aspx?cid=2">优势品牌</a></li>
          <li><a href="distribution_brand.aspx?cid=3">经销品牌</a></li>
          <li><a href="pro_classification.aspx?cid=4">产品分类</a></li>
          <li><a href="industry.aspx?cid=5">行业分类</a></li>
        </ul>
      </div>
      <div class="item">
        <h3><a href="acting_brand.aspx">产品中心</a></h3>
        <ul>
          <li><a href="acting_brand.aspx?cid=1">代理品牌</a></li>
          <li><a href="advantage_brand.aspx?cid=2">优势品牌</a></li>
          <li><a href="distribution_brand.aspx?cid=3">经销品牌</a></li>
          <li><a href="pro_classification.aspx?cid=4">产品分类</a></li>
          <li><a href="industry.aspx?cid=5">行业分类</a></li>
        </ul>
      </div>




    </div>

  </div>
</template>

<style>
@import "//at.alicdn.com/t/font_1087576_1x9nz1xqvrw.css";
#app {
  font-family: 'Avenir', Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
}


.head {
  margin: 0 auto;
  max-width: 1080px;
  height: 100px;
}


.head .logo {
  float: left;
  margin-top: 5px;
}
.head .logo > img {
  height: 90px;
  
}
.head .menu {
  float: right;
  margin-top: 10px;
  margin-right: 50px;
}
.head > .body::after {
  content: ' ';
  clear: both;
}
.fiex {
  position: fixed;
  top: 0;
  left: 0;
  right: 0;
  border-bottom: 1px solid #ededee;
  background-color: #fff;
}

.menu > ul {
  list-style: none;
}
.menu > ul li {
  margin-left: 50px;
  display: inline-block;
}
.menu > ul li i {
  font-size: 30px;
}
.menu > ul li a {
    color: #666;
    display: inline-block;
}
.body {
  max-width: 1080px;
  margin: 100px auto 0;
  padding: 50px 0;
}


.foot {
  display: flex;
  justify-content: center;
  background-color: #f0f0f0;
  min-width: 1080px;
  padding-bottom: 50px;
}
.foot > .item {
  border-left: 1px solid #dcdcdc;
  margin: 20px  5px;
  padding: 0 20px;
}
.foot > .item > ul  {
  list-style: none;
  margin: 0;
}
.foot > .item > h3  {
  margin: 0;
}
.foot > .item a  {
  color: #777;
}
.foot-log {
  text-align: left;
  margin: 25px 20px;
}
.foot-log > img {
  height: 60px;
}
body {
  margin: 0;
}
a {
  text-decoration: none;
}
ul {
  padding-left: 0;
}
</style>
