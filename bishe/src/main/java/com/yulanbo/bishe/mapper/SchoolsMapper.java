package com.yulanbo.bishe.mapper;

import com.yulanbo.bishe.model.Schools;
import com.yulanbo.bishe.model.User;
import org.apache.ibatis.annotations.Mapper;

import java.util.List;

@Mapper
public interface SchoolsMapper {
    int insert(Schools record);
    List<Schools> getSchools();
    int insertSelective(Schools record);
}