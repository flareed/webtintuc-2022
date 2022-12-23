<template>
    <HomeHeader />
    <main>
        <div class="editor-style">
            <div class="mb-3">
                <label for="title" class="form-label">Tiêu đề</label>
                <input type="text" class="form-control" id="title" v-model="title">
            </div>
            <div class="mb-3">
                <label for="titleImage" class="form-label">Ảnh tiêu đề</label>
                <input type="file" class="form-control" id="titleImage" @change="selectFile" ref="fileInput">
            </div>
            <div class="mb-3">
                <label for="description" class="form-label">Mô tả ngắn</label>
                <textarea type="text" class="form-control" id="description" v-model="description" rows="3"></textarea>
            </div>
            <div class="mb-3">
                <label for="author" class="form-label">Tác giả (hoặc trích dẫn)</label>
                <input type="text" class="form-control" id="author" v-model="author">
            </div>
            <div class="mb-3">
                <label for="location" class="form-label">Địa điểm</label>
                <input type="text" class="form-control" id="location" v-model="location">
            </div>
            <div class="mb-3">
                <label for="tag">Tag</label>
                <select class="form-select" v-model="tag" id="tag">
                    <option v-for="item in this.categories" :key="item.name">
                        {{ item.name }}
                    </option>
                </select>
            </div>
            <ckeditor :editor="editor" v-model="editorData" :config="editorConfig"></ckeditor>
            <button type="button" class="btn btn-success mt-4 float-end" data-bs-toggle="modal"
                data-bs-target="#exampleModal" @click="onSubmit()">
                Submit
            </button>


            <!-- Modal -->
            <div class="modal fade" id="exampleModal" tabindex="-1" aria-labelledby="exampleModalLabel"
                aria-hidden="true">
                <div class="modal-dialog">
                    <div class="modal-content">
                        <div class="modal-header">
                            <h1 class="modal-title fs-5" id="exampleModalLabel">Thông báo</h1>
                            <button type="button" class="btn-close" data-bs-dismiss="modal" aria-label="Close"></button>
                        </div>
                        <div class="modal-body">
                            <div v-if="success">
                                Submit thành công
                            </div>
                            <div v-else>
                                Submit không thành công, có lỗi xảy ra
                            </div>
                            
                        </div>
                        <div class="modal-footer">
                            <button type="button" class="btn btn-secondary" data-bs-dismiss="modal">Đóng</button>
                        </div>
                    </div>
                </div>
            </div>

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
import { HTTP } from '../api'
import axios from 'axios';

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
            image: '',
            description: '',
            author: '',
            location: '',
            tag: '',
            categories: [],
            success: true
        };
    },
    methods: {
        selectFile(event) {
            this.image = event.target.files[0]
        },
        onSubmit() {
            let categoryId = this.categories.find(
                (destination) => destination.name === this.tag
            ).id

            const formData = new FormData();
            formData.append('category', categoryId);
            formData.append('author', this.author);
            formData.append('title', this.title);
            formData.append('description', this.description);
            formData.append('content', this.editorData);
            formData.append('location', this.location);
            formData.append('img', this.image);

            HTTP.post(`/api/articles/`,
                formData
            ,{
                headers: {
                    'Content-Type': 'multipart/form-data'
                }
            })
                .then(response => { 
                   console.log(response)
                })
                .catch(e => {
                    this.success = false
                    console.log(e.response.data)
                })

            this.title = ''
            this.image = ''
            this.description = ''
            this.author = ''
            this.location = ''
            this.tag = ''
            this.editorData = ''
            this.$refs.fileInput.value = null
        }
    },
    created() {
        HTTP.get(`api/categories/`)
            .then(response => {
                this.categories = response.data.results
                axios.get(response.data.next)
                    .then(res => {
                        this.categories.push(...res.data.results)
                    })
                    .catch(e => {
                        console.log(e)
                    })
            })
            .catch(e => {
                this.success = false
                console.log(e)
            })
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