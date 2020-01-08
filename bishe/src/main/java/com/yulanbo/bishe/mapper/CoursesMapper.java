package com.yulanbo.bishe.mapper;

import com.yulanbo.bishe.model.Courses;
import org.apache.ibatis.annotations.Mapper;

@Mapper
public interface CoursesMapper {
    int insert(Courses record);

    int insertSelective(Courses record);
}