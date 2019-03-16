<template>
  <div class="prod-list">
    <div class="prod" v-for="d in ds" :key="d.name">
      <div class="prod-img">
        <img :src="'/prodImg/' + d.name + '.png'">
      </div>
      <div class="prod-title">{{d.title}}</div>
    </div>
  </div>
</template>

<script>
export default {
  name: "productCentre",
  data() {
    return {
      ds: [
        {
          name: "ROEMHELD",
          title: "德国罗姆希特ROEMHELD"
        },
        {
          name: "CABUR",
          title: "CABUR"
        },
        {
          name: "AMF",
          title: "德国AMF油压缸"
        },
        {
          name: "BETE",
          title: "美国BETE喷嘴"
        },
        {
          name: "FEIN",
          title: "德国FEIN泛音"
        },
        {
          name: "Italvibras",
          title: "意大利Italvibras 振动电机"
        },
        {
          name: "PAULY",
          title: "德国PAULY宝丽"
        },
        {
          name: "MAHLE",
          title: "德国MAHLE马勒"
        },
        {
          name: "ZIMMER",
          title: "德国ZIMMER夹具"
        },
        {
          name: "TIEFENBACH",
          title: "德国TIEFENBACH帝芬巴赫阀"
        },
        {
          name: "TOGNELLA",
          title: "意大利TOGNELLA多利拿液压阀"
        },
        {
          name: "LIST-MAGNETIK",
          title: "德国LIST-MAGNETIK充磁器"
        },
        {
          name: "KABELSCHLEPP",
          title: "德国KABELSCHLEPP佳宝来 拖链"
        },
        {
          name: "LENORD+BAUER",
          title: "德国LENORD+BAUER 编码器"
        }
      ]
    };
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