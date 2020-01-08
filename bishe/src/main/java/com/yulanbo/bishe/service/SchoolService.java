package com.yulanbo.bishe.service;

import com.yulanbo.bishe.model.Schools;
import com.yulanbo.bishe.model.User;
import org.springframework.stereotype.Service;

import java.util.List;

@Service
public interface SchoolService {
    List<Schools> getSchools();
}
