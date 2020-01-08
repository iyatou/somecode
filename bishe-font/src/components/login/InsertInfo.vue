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
		height: 430px;
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
			<h2>绑定信息</h2>
			<Form ref="InsertInfo" :model="InsertInfo" :label-width="80">
				<FormItem label="Name">
					<Input type="text" v-model="InsertInfo.username" placeholder="请输入姓名"></Input>
				</FormItem>
                <FormItem label="Sex">
                    <RadioGroup v-model="InsertInfo.sex">
                        <Radio label="boy" style="margin-right: 50px;">
                            <Icon type="md-male" />
                            <span>男</span>
                        </Radio>
                        <Radio label="girl">
                            <Icon type="md-female" />
                            <span>女</span>
                        </Radio>
                    </RadioGroup>
                </FormItem>
                <FormItem label="Birthday">
                    <Col span="12">
                        <Date-picker  placeholder="选择日期" style="width:200px;" type="datetime" v-model="InsertInfo.birthday"  format="yyyy-MM-dd"  @on-change="InsertInfo.birthday=$event" >
                        </Date-picker> 
                    </Col>
                </FormItem>
                <FormItem label="School">
                    <Select v-model="InsertInfo.school" filterable style="width: 200px;margin-left: -60px;">
                        <Option v-for="item in cityList" :value="item.name" :key="item.id">{{item.name}}</Option>
                    </Select>
                </FormItem>
                <FormItem label="Identify">
                    <RadioGroup v-model="InsertInfo.identify" type="button" >
                        <Radio label="教师" style="margin-right: 30px;"></Radio>
                        <Radio label="学生" ></Radio>
                    </RadioGroup>
                </FormItem>  
				<FormItem class="form-footer">
					<Button type="primary" @click="handleSubmit">绑定</Button>
				</FormItem>
			</Form> 
		</div>
	</div>
</template>
<script>
	export default {
		data() {
			return {
				dis:false,
				count:'',
				timer:null,
                cityList:[],
                InsertInfo:{
                    useremail:'',
                    username:'',
                    sex:'boy',
                    birthday:'',
                    identify:'',
                    school:'',
                }
			}
		},
        mounted(){
            this.getRouteData()
        },
		methods: {
			getRouteData(){
                this.InsertInfo.useremail=this.$route.query.useremail
                console.log(this.InsertInfo.useremail)
                this.$axios.get('/getschool').then((response) =>{
                    this.cityList=response.data
                }).catch((error) =>{
                    console.log(error)
                })
                console.log(this.cityList)
            },
			goLogin() {
				this.$router.push({ path: '/' })
			},
			handleSubmit() {
				if(this.InsertInfo.username==""){
                    this.$Message.error("请输入姓名!")
                    return
                }
                if(this.InsertInfo.birthday==""){
                    this.$Message.error("请选择出生日期!")
                    return
                }
                if(this.InsertInfo.school==""){
                    this.$Message.error("请选择学校!")
                    return
                }
                if(this.InsertInfo.identify==""){
                    this.$Message.error("请选择身份")
                    return
                }
                this.$axios.post('/bindinfo',this.InsertInfo).then((response) => {
					if(response.data=="ok"){
						if(this.InsertInfo.identify=="学生"){
							this.$router.push({path:'student'})
						}
						if(this.InsertInfo.identify=="教师"){
							this.$router.push({path:'teacher'})
						}
					}
					else{
						this.$Message.error("修改失败！")
						return
					}
				}).catch((error) =>{
					console.log(error)
				})
			},
		}
	}
</script>