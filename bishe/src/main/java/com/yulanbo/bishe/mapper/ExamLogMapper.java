package com.yulanbo.bishe.mapper;

import com.yulanbo.bishe.model.ExamLog;
import org.apache.ibatis.annotations.Mapper;

@Mapper
public interface ExamLogMapper {
    int insert(ExamLog record);

    int insertSelective(ExamLog record);
}