package com.yulanbo.bishe.mapper;

import com.yulanbo.bishe.model.User;
import org.apache.ibatis.annotations.Mapper;

@Mapper
public interface UserMapper {
    User checkUser(String useremail,String password);
    int insertSelective(User record);
    int addUser(User user);
    int alterPass(User user);
    int bindInfo(User user);
    User selectByEmail(String useremail);
}