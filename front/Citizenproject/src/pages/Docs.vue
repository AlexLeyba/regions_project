<template>
  <div class="inner_content">
    <div class="content_block doc_block">
      <p class="inner_header">Нормативные документы</p>
      <a class="back_link" @click="$router.go(-1)"><img alt="" class="back_arrow" src="../../imgs/back2.png">Вернуться
        назад
      </a>
      <div class="documents">

        <div v-for="(item, index) in all_docs" ref="doc_item" :key="index" class="doc_item">
          <p class="doc_item_type">{{item.ico}}</p>
          <a :href="item.file">{{item.title}}</a>
          <div class="doc_item_descr">{{item.desc}}</div>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
  export default {
    name: "About",
    data() {
      return {
        all_docs: []
      }
    },
    beforeMount() {
      this.loadDocs()
    },
    methods: {
      loadDocs: function () {

        this.$http.get('https://cfo.admlr.lipetsk.ru/citizen/docks')
          .then(response => {
            return response.json()
          })
          .then(docs => {
            this.all_docs = docs.results
            console.log('this.all_docs', this.all_docs)

            this.all_docs.forEach(function (item) {
              let fileUrl = item.file,
                parts, ext = (parts = fileUrl.split("/").pop().split(".")).length > 1 ? parts.pop() : "";
                console.log('ext', ext)
              switch (ext) {
                case 'pdf':
                  item.ico = "PDF";
                  break;
                case 'xls':
                  item.ico = "XLS";
                  break;
                case 'xlsx':
                  item.ico = "XLSX";
                  break;
                case 'doc':
                  item.ico = "DOC";
                  break;
                case 'docx':
                  item.ico = "DOCX";
                  break;
                case 'jpg':
                  item.ico = "JPG";
                  break;
                case 'png':
                  item.ico = "PNG";
                  break;
                default:
                  item.ico = "FILE";
                  break;
              }
             if (item.desc) item.desc=item.desc.slice(0, 251)+'...'
              console.log('item', item)
            })
          })
        // this.all_docs=[
        //   {id:1, title: 'Безусловно, современная методология разработки однозначно определяет каждого', file: 'https://st2.depositphotos.com/2111141/5308/i/450/depositphotos_53087525-stock-photo-handsome-guy.xlsx'},
        //   {id:2, title: 'Безусловно, современная методология разработки однозначно определяет каждого2', file: 'https://cdn.trinixy.ru/pics5/20160811/beautiful_girls_06.jpg'},
        //   {id:2, title: 'Безусловно, современная методология разработки однозначно определяет каждого3', file: 'https://cdn.trinixy.ru/pics5/20160811/beautiful_girls_06.bmp'}
        // ]
      }
    }
  }
</script>

<style scoped>

</style>
