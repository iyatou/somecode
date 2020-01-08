package com.yulanbo.bishe.mapper;

import com.yulanbo.bishe.model.Homework;
import org.apache.ibatis.annotations.Mapper;

@Mapper
public interface HomeworkMapper {
    int insert(Homework record);

    int insertSelective(Homework record);
}