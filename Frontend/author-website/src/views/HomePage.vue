<template>
    <HomeHeader />
    <main>
        <div class="editor-style">
            <div class="form-group">
                <label for="title">Tiêu đề</label>
                <input type="text" id="title" v-model="title" class="form-control">
            </div>
            <div class="form-group">
                <label for="title">Ảnh tiêu đề (link)</label>
                <input type="text" id="titleImage" v-model="titleImage" class="form-control">
            </div>
            <div class="form-group mt-3">
                <label for="description">Mô tả ngắn</label>
                <textarea type="text" id="description" v-model="description" class="form-control" rows="3"></textarea>
            </div>
            <div class="form-group mt-3">
                <label for="author">Tác giả (hoặc trích dẫn)</label>
                <input type="text" id="author" v-model="author" class="form-control">
            </div>
            <div class="form-group mt-3">
                <label for="location">Địa điểm</label>
                <input type="text" id="location" v-model="location" class="form-control">
            </div>
            <div class="form-group mt-3">
                <label for="tag">Tag</label>
                <select name="tag" class="form-control" v-model="tag" id="tag">
                    <option>Thời sự</option>
                    <option>Khoa học</option>
                    <option>Số hoá</option>
                    <option>Sức khoẻ</option>
                </select>
            </div>
            <ckeditor :editor="editor" v-model="editorData" :config="editorConfig"></ckeditor>
            <input type="button" value="Submit" class="btn btn-success mt-4 float-right" @click="onSubmit()">
        </div>
    </main>

    <br>
    <br>
    <br>
    <HomeFooter />
</template>
  
<script>
import ClassicEditor from '@ckeditor/ckeditor5-build-classic';
import HomeHeader from '../components/HomeHeader.vue'
import HomeFooter from '../components/HomeFooter.vue'

export default {
    name: 'HomePage',
    data() {
        return {
            editor: ClassicEditor,
            editorData: '<p>Content of the editor.</p>',
            editorConfig: {
                // The configuration of the editor.
            },
            title: '',
            titleImage: '',
            description: '',
            author: '',
            location: '',
            tag: ''
        };
    },
    methods: {
        onSubmit() {
            let article = {
                "title": this.title,
                "imageTitle": this.imageTitle,
                "description": this.description,
                "author": this.author,
                "location": this.location,
                "tag": this.tag,
                "content": this.editorData
            }
            console.log(article)
            this.title = ''
            this.imageTitle = ''
            this.description = ''
            this.author = ''
            this.location = ''
            this.tag = ''
            this.editorData = ''
        }
    },
    components: {
        HomeHeader,
        HomeFooter
    },
}
</script>
  
  <!-- Add "scoped" attribute to limit CSS to this component only -->
<style>
.ck-editor__editable {
    min-height: 500px !important;
}

.editor-style {
    padding-top: 20px !important;
    padding-left: 10% !important;
    padding-right: 10% !important;
}
</style>