import VueRouter from 'vue-router';
import Listing from './components/Listing'
import Details from './components/Details'
import Create from './components/Create'



const  routes=[
    {
        name:'index',
        path:'/',
        component:Listing,
    },
    {
        name:'detail',
        path:'/detail/:slug',
        component:Details
    },
    {
        name:'create',
        path:'/create',
        component:Create
    }
]
const router = new VueRouter({
    mode:'history',
    routes:routes
})

export default router;