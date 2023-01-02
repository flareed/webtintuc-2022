import { reactive } from "vue";

export const store = reactive({
    selectedCategory: 0,
    currentUser: {},
    isAuthenticate: false,
    login(data){
        this.currentUser = data;
        this.isAuthenticate = true;
    },
    logout(){
        this.currentUser = {};
        this.isAuthenticate = false;
    },
})
