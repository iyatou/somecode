<style scoped>
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
		margin-top: -250px;
		width: 400px;
		height: 350px;
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
			linesColor="#dedede" :linesWidth="1" :lineLinked="true" :lineOpacity="0.4" :linesDistance="150"
			:moveSpeed="3" :hoverEffect="true" hoverMode="grab" :clickEffect="true" clickMode="push">
		</vue-particles>
		<div class="from-wrap">
			<h2>修改密码</h2>
			<Form ref="RegisterData" :model="RegisterData" :label-width="80">
				<FormItem label="Email">
					<Input type="text" v-model="RegisterData.useremail" placeholder="请输入邮箱"></Input>
				</FormItem>
				<FormItem label="Password">
					<Input type="password" v-model="RegisterData.password" placeholder="请输入新密码"></Input>
				</FormItem>
				<FormItem label="Repassword">
					<Input type="password" v-model="RegisterData.repassword" placeholder="请再次输入新密码"></Input>
				</FormItem>
				<FormItem label="code">
					<Input type="number" v-model="RegisterData.code" placeholder="请输入验证码"
						style="width: 150px;margin-right: 5px;"></Input>
					<Button :disabled="dis" type="primary" @click="getCode" style="margin-right: -1px;">{{content}}</Button>
				</FormItem>
				<FormItem class="form-footer">
					<Button type="primary" @click="handleSubmit">修改</Button>
				</FormItem>
			</Form>
		</div>
	</div>
</template>
<script>
	export default {
		data() {
			return {
				content: "获取验证码",
				dis:false,
				count:'',
				timer:null,
				RegisterData: {
					useremail: '',
					password: '',
					repassword: '',
					code: "",
				},
			}
		},
		methods: {
			getCode() {
				
				var regEmail = /^([a-zA-Z0-9]+[_|\_|\.]?)*[a-zA-Z0-9]+@([a-zA-Z0-9]+[_|\_|\.]?)*[a-zA-Z0-9]+\.[a-zA-Z]{2,3}$/;
				if (!regEmail.test(this.RegisterData.useremail)) {
					this.$Message.info("邮箱格式不正确！")
					return
				}
				const TIME_COUNT = 120;
				if (!this.timer) {
					this.count = TIME_COUNT;
					this.timer = setInterval(() => {
						this.dis=true
						if (this.count > 0 && this.count <= TIME_COUNT) {
							this.count--;
							this.content="等待"+this.count+"秒"
						} else {
							this.content="获取验证码"
							clearInterval(this.timer);
							this.timer = null;
							this.dis=false
						}
					}, 1000)
				}
				this.$axios.get('/getcode', {
					params: {
						useremail: this.RegisterData.useremail
					},
				}).then((response) => {
				}).catch((error) => {
					console.log(error)
				});
			},
			goLogin() {
				this.$router.push({ path: '/' })
			},
			handleSubmit() {
				if (this.RegisterData.useremail == "") {
					this.$Message.error("邮箱不能为空");
					return
				}

				if (this.RegisterData.password == "") {
					this.$Message.error("密码不能为空");
					return
				}
				let checkpassword = /^(?=.*?[A-Z])(?=.*?[a-z])(?=.*?[0-9])[A-Za-z0-9]{8,16}$/;
				if (!checkpassword.test(this.RegisterData.password)) {
					this.$Message.error("密码必须是包含大小写字母和数字，长度8-16位")
				}
				if (this.RegisterData.repassword == "") {
					this.$Message.error("重复密码不能为空");
					return
				}
				if (this.RegisterData.password != this.RegisterData.repassword) {
					this.$Message.error("两次密码不一致")
					return
				}
				if (this.RegisterData.code == "") {
					this.$Message.error("验证码不能为空");
					return
				}
				this.$axios.post('/alterpass', this.RegisterData)
					.then((response) => {
						let info = response.data
						console.log(response)
						if (response.data == 'ok') {
							this.$Message.info("修改成功！")
							this.$router.push({ path: '/' })
						}
						if (response.data == 'codeerror') {
							console.log(123123)
							this.$Message.error("验证码错误")
						}
						if (response.data == 'fail') {
							this.$Message.error("该用户名不存在")
						}
					}).catch((error) => {
						console.log(error)
					});
			},
		}
	}
</script>