<style>
  html,
  body {
    width: 100%;
    height: 100%;
    background-color: #1c2438;
  }

  .login {
    width: 100%;
    height: 100%;
    background-color: #1c2438;
    position: relative;
  }

  .login .from-wrap {
    position: fixed;
    left: 50%;
    margin-left: -200px;
    top: 50%;
    margin-top: -150px;
    width: 400px;
    height: 240px;
    border-radius: 10px;
    background-color: #fff;
    padding: 20px 30px;
  }

  .login h2 {
    text-align: center;
    margin-bottom: 20px;
  }

  .login FormItem {
    margin-bottom: 15px;
  }

  .login .form-footer {
    text-align: right;
  }

  .ivu-form-item-required .ivu-form-item-label:before {
    display: none;
  }
</style>
<template>
  
  <div class="login">
    
    <vue-particles color="#dedede" :particleOpacity="0.7" :particlesNumber="80" shapeType="circle" :particleSize="4"
      linesColor="#dedede" :linesWidth="1" :lineLinked="true" :lineOpacity="0.4" :linesDistance="150" :moveSpeed="3"
      :hoverEffect="true" hoverMode="grab" :clickEffect="true" clickMode="push">
    </vue-particles>
    <div class="from-wrap">
      <h2>登录</h2>
      <Form ref="loginData" :model="loginData" :label-width="80">
        <FormItem label="Email" on-blur="checkemail">
          <Input type="text" v-model="loginData.useremail" placeholder="请输入账号"></Input>
        </FormItem>
        <FormItem label="Password">
          <Input type="password" v-model="loginData.password" minlength="8" maxlength="16" placeholder="请输入密码"></Input>
        </FormItem>
          
        <FormItem class="form-footer">
          <a style="margin-right:60px;" @click="alterpass">忘记密码</a>
          <Button type="primary" @click="handleSubmit">登录</Button>
          <Button type="default" @click="goToRegister" style="margin-left: 8px">注册</Button>
        </FormItem>
      </Form>
      
    </div>
    
  </div>
</template>
<script>
  export default {
    data() {
      return {
        loginData: {
          useremail: '',
          password: ''
        },
      }
    },
    methods: {
      alterpass(){
        this.$router.push({ path: 'alterpass' })
      },
      handleSubmit() {
        var regEmail= /^([a-zA-Z0-9]+[_|\_|\.]?)*[a-zA-Z0-9]+@([a-zA-Z0-9]+[_|\_|\.]?)*[a-zA-Z0-9]+\.[a-zA-Z]{2,3}$/;
        if(!regEmail.test(this.loginData.useremail)){
          this.$Message.info("邮箱格式不正确！")
          return
        }
        this.$axios.post('/login', this.loginData)
          .then((response) => {
            let info=response.data
            if(info.data=='success'){
              if(info.identify=="学生"){
                this.$router.push({path:'student'})
                this.$Message.info("登录成功！")
              }
              if(info.identify=="教师"){
                this.$router.push({path:'teacher'})
                this.$Message.info("登录成功！")
              }
              if(info.identify==""){
                this.$Message.info("您是第一次登录，请绑定信息！")
                this.$router.push({path:'/insertinfo',query:{useremail:this.loginData.useremail}})
              }
            }
            else{
              this.$Message.error("账号或密码错误！")
            }
          }).catch((error) => {
            console.log(error)
          });
      },
      goToRegister(){
        this.$router.push({path:'register'})
      }
    }
  }
</script>