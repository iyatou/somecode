package com.yulanbo.bishe.service;

import com.yulanbo.bishe.model.User;
import org.apache.el.parser.BooleanNode;
import org.springframework.stereotype.Service;

@Service
public interface UserService {
    public User checkUser(String useremail, String password);
    public int addUser(User user);
    public int alterPass(User user);
    public int bindInfo(User user);
    public User selectByEmail(String useremail);
}
