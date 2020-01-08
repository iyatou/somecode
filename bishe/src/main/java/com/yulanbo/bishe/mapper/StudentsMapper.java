package com.yulanbo.bishe.mapper;

import com.yulanbo.bishe.model.Students;
import org.apache.ibatis.annotations.Mapper;

@Mapper
public interface StudentsMapper {
    int insert(Students record);

    int insertSelective(Students record);
}