<template>
  <div class="prod-list">
    <div class="prod" v-for="(d, i) in ds" :key="d.name" @click="showProdInfo(i)">
      <div class="prod-img">
        <img :src="'/prodImg/' + d.name + '.png'">
      </div>
      <div class="prod-title">{{d.title}}</div>
    </div>
  </div>
</template>

<script>
import store from "../js/store.js"
export default {
  name: "productCentre",
  data() {
    return {
      ds: store.prods
    };
  },
  methods: {
    showProdInfo(i) {
      this.$router.push(`/productInfo/${i}`)
    }
  }
};
</script>

<style scoped>
.prod-list {
  height: inherit;
  display: flex;
  flex-wrap: wrap;
}

.prod {
  height: 150px;
  width: 180px;
  border: 1px solid #e4e4e4;
  margin-left: 15px;
  margin-top: 15px;
  transition: all ease-in-out 200ms;
  cursor: pointer;
}
.prod:hover {
  border: 1px solid #007cc2;
}
.prod-img {
  height: 130px;
  line-height: 130px;
}
.prod-img > img {
  max-height: 122px;
  max-width: 180px;
  vertical-align: middle;
}
.prod-title {
  white-space: nowrap;
  text-overflow: ellipsis;
  overflow: hidden;
  font-size: 12px;
  color: #999;
}
</style>