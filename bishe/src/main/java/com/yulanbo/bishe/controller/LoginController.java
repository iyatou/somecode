package com.yulanbo.bishe.controller;

import com.fasterxml.jackson.databind.JsonSerializer;
import com.fasterxml.jackson.databind.util.JSONPObject;
import com.sun.net.httpserver.HttpServer;
import com.yulanbo.bishe.model.Schools;
import com.yulanbo.bishe.model.User;
import com.yulanbo.bishe.receiveInfo.BindInfo;
import com.yulanbo.bishe.receiveInfo.LoginInfo;
import com.yulanbo.bishe.receiveInfo.RegisterInfo;
import com.yulanbo.bishe.responseinfo.LoginRes;
import com.yulanbo.bishe.responseinfo.MailService;
import com.yulanbo.bishe.service.SchoolService;
import com.yulanbo.bishe.service.UserService;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Controller;
import org.springframework.web.bind.annotation.*;

import javax.servlet.http.HttpServletRequest;
import javax.servlet.http.HttpSession;
import java.text.DateFormat;
import java.text.SimpleDateFormat;
import java.util.*;

@Controller
public class LoginController {
    @Autowired
    UserService userService;

    @Autowired
    MailService mailService;

    @Autowired
    SchoolService schoolService;
//    登录
    @ResponseBody
    @RequestMapping(value = "/login", method = RequestMethod.POST, produces = "application/json;charset=UTF-8")
    public LoginRes Login(@RequestBody LoginInfo logininfo){
        String useremail=logininfo.getUseremail();
        String password=logininfo.getPassword();
        User user=userService.checkUser(useremail,password);
        if(user!=null){
            LoginRes loginRes= new LoginRes();
            loginRes.setData("success");
            loginRes.setUsername(user.getUsername());
            loginRes.setIdentify(user.getIdentity());
            return loginRes;
        }
        else{
            LoginRes loginRes= new LoginRes();
            loginRes.setData("fail");
            return loginRes;
        }
    }
    //注册
    @ResponseBody
    @RequestMapping(value="/register",method=RequestMethod.POST,produces = "application/json;charset=UTF-8")
    public String Register(@RequestBody RegisterInfo registerInfo, HttpServletRequest request){
        User find=userService.selectByEmail(registerInfo.getUseremail());

        HttpSession session = request.getSession();
        String myRedisSession = (String) request.getSession().getAttribute("code");
        if(find==null){
            if(!registerInfo.getCode().equals(myRedisSession)){
                return "codeerror";
            }
            else{
                User user=new User();
                user.setUseremail(registerInfo.getUseremail());
                user.setPassword(registerInfo.getPassword());
                userService.addUser(user);
                return "ok";
            }
        }
        else{
            return "fail";
        }
    }

    //获取验证码
    @ResponseBody
    @RequestMapping(value="/getcode",method = RequestMethod.GET,produces = "application/json;charset=UTF-8")
    public String getCode(@RequestParam String useremail, HttpServletRequest request) throws Exception{
        String checkCode = String.valueOf(new Random().nextInt(899999) + 100000);
        String sender=useremail;
        try {
            mailService.sendSimpleMail(sender,checkCode);
            System.out.println("调用service");
        }catch (Exception e){
            System.out.println(e);
            return "发送失败";
        }
        request.getSession().setAttribute("code", checkCode);
        request.getSession().setMaxInactiveInterval(2*60);
        return "已发送";
    }

    //修改密码
    @ResponseBody
    @RequestMapping(value = "/alterpass",method = RequestMethod.POST,produces = "application/json;charset=UTF-8")
    public String alterPass(@RequestBody RegisterInfo registerInfo, HttpServletRequest request){
        User find=userService.selectByEmail(registerInfo.getUseremail());
        HttpSession session = request.getSession();
        String myRedisSession = (String) request.getSession().getAttribute("code");
        if(find!=null){
            if(myRedisSession.equals(registerInfo.getCode())){
                User user=new User();
                user.setUseremail(registerInfo.getUseremail());
                user.setPassword(registerInfo.getPassword());
                userService.alterPass(user);
                return "ok";
            }
            else{
                return "codeerror";
            }
        }
        else{
            return "none";
        }
    }
    @ResponseBody
    @RequestMapping(value="/getschool",method = RequestMethod.GET,produces = "application/json;charset=UTF-8")
    public List<Schools> getSchool(HttpServletRequest request) throws Exception{
        return schoolService.getSchools();
    }

    @ResponseBody
    @RequestMapping(value = "/bindinfo",method = RequestMethod.POST,produces = "application/json;charset=UTF-8")
    public String bindInfo(@RequestBody BindInfo bindInfo,HttpServletRequest request) throws Exception{
        User user=new User();
        DateFormat format1 = new SimpleDateFormat("yyyy-MM-dd");
        Date date = null;
        date = format1.parse(bindInfo.getBirthday());
        user.setUsername(bindInfo.getUsername());
        user.setSchool(bindInfo.getSchool());
        user.setSex(bindInfo.getSex());
        user.setIdentity(bindInfo.getIdentify());
        user.setBirthday(date);
        user.setUseremail(bindInfo.getUseremail());
        try{
            userService.bindInfo(user);
        }catch(Exception e){
            System.out.println(e);
            return "fail";
        }
        return "ok";
    }
}
