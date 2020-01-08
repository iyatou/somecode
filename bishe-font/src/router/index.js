import Vue from 'vue'
import Router from 'vue-router'
import Login from '@/components/login/Login'
import Register from '@/components/login/Register'
import Alterpass from '@/components/login/AlterPass'
import Insertinfo from '@/components/login/InsertInfo'
import Studentmain from '@/components/student/StudentMain'
import Teachermain from '@/components/teacher/TeacherMain'

Vue.use(Router)

export default new Router({
  routes: [
    {
      path: '/',
      name: 'Login',
      component: Login
    },
    {
      path:'/register',
      name:'Register',
      component:Register
    },
    {
      path:'/alterpass',
      name:'Alterpass',
      component:Alterpass
    },
    {
      path:'/insertinfo',
      name:'Insertinfo',
      component:Insertinfo
    },
    {
      path:'/student',
      name:'Studentmain',
      component:Studentmain
    },
    {
      path:'/teacher',
      name:'Teachermain',
      component:Teachermain
    }
  ]
})
