<template>
  <div class="prod-info">
    <h1>{{title}}</h1>
    <div class="imgAndInfo">
      <div class="img">
        <img :src="'/prodImg/' + name + '.png'">
      </div>
      <div class="info">
        <h3>品牌简介</h3>
        <div v-html="infoMk" class="markdown-body"></div>
      </div>
    </div>
    <div class="type">
      <h3>产品型号</h3>
      <div>
        <pre>{{type}}</pre>
      </div>
    </div>
  </div>
</template>

<script>
import store from "../js/store.js";
import marked from "marked";
import 'github-markdown-css'
export default {
  name: "productInfo",
  data() {
    return {
      name: "",
      title: "",
      info: "",
      type: ""
    };
  },
  computed: {
    infoMk() {
      return marked(this.info, { sanitize: true })
    }
  },
  beforeRouteUpdate(to, from, next) {
    this.loadProd(to.params.id);
  },
  methods: {
    loadProd(id) {
      let prod = store.prods[id];
      this.title = prod.title;
      this.name = prod.name;
      let _this = this;
      this.axios.get(`/prodInfo/${prod.name}.md`).then(function(r) {
        _this.info = r.data;
      });
      this.axios.get(`/prodType/${prod.name}.txt`).then(function(r) {
          _this.type = r.data;
        });
    }
  },
  mounted: function() {
    this.$nextTick(function() {
      this.loadProd(this.$route.params.id);
    });
  }
};
</script>

<style scoped>

.prod-info {
  padding: 20px;
}
.prod-info > h1 {
  text-align: left;
}
.imgAndInfo::after {
  content: "";
  clear: both;
  display: block;
}
.img {
  float: left;
  height: 236px;
  width: 262px;
  border: 1px solid #eaeaea;
  line-height: 236px;
}
.img > img {
  max-width: 262px;
  max-height: 236px;
  vertical-align: middle;
}
.info {
  float: right;
  width: 850px;
}
.info > h3 {
  margin-top: 0;
  background-color: #007cc2;
  color: #fff;
  text-align: left;
  padding: 10px;
}
.info div {
  text-align: left;
}
.type h3 {
  background-color: #f2f2f2;
  color: #007cc2;
  text-align: left;
  padding: 10px;
}
.type div {
  text-align: left;
}
pre {
  font-family: "Avenir", Helvetica, Arial, sans-serif;
}
</style>