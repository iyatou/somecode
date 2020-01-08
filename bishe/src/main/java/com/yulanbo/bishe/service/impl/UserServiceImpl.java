package com.yulanbo.bishe.service.impl;

import com.yulanbo.bishe.mapper.UserMapper;
import com.yulanbo.bishe.model.User;
import com.yulanbo.bishe.service.UserService;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Service;

@Service
public class UserServiceImpl implements UserService {

    @Autowired
    UserMapper userMapper;
    @Override
    public User checkUser(String useremail, String password) {
        return userMapper.checkUser(useremail,password);
    }

    @Override
    public int addUser(User user){
        return userMapper.addUser(user);
    }

    @Override
    public User selectByEmail(String useremail){
        return userMapper.selectByEmail(useremail);
    }

    @Override
    public int alterPass(User user){return userMapper.alterPass(user);}

    @Override
    public int bindInfo(User user){return userMapper.bindInfo(user);}
}
