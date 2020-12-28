<template>
  <img :src="imagePath" class="minimized" alt="" ref="minimized" @click="ImageClick">
</template>

<script>
  export default {
    name: "Gallery",
    props: ['imagePath'],
    data: function () {
      return {

      }
    },
    methods: {
      ImageClick: function (event) {
        //console.log('item ',event)
        let i_path=event.srcElement.currentSrc;
        console.log('i_path ',i_path)
        // генерируем событие 'remove' и передаём id элемента
        this.$emit('showImage', i_path);
        //console.log(this.$refs.bigImage)
      }
    }
  }
</script>

<style scoped>

</style>
