package com.yulanbo.bishe.mapper;

import com.yulanbo.bishe.model.CourseEffict;
import org.apache.ibatis.annotations.Mapper;

@Mapper
public interface CourseEffictMapper {
    int insert(CourseEffict record);

    int insertSelective(CourseEffict record);
}