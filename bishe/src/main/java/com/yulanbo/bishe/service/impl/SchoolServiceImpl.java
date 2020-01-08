package com.yulanbo.bishe.service.impl;

import com.yulanbo.bishe.mapper.SchoolsMapper;
import com.yulanbo.bishe.model.Schools;
import com.yulanbo.bishe.model.User;
import com.yulanbo.bishe.service.SchoolService;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Service;

import java.util.List;

@Service
public class SchoolServiceImpl implements SchoolService {
    @Autowired
    SchoolsMapper schoolsMapper;
    @Override
    public List<Schools> getSchools() {
        return schoolsMapper.getSchools();
    }
}
