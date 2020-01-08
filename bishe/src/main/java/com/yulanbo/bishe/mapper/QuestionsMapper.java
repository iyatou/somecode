package com.yulanbo.bishe.mapper;

import com.yulanbo.bishe.model.Questions;
import org.apache.ibatis.annotations.Mapper;

@Mapper
public interface QuestionsMapper {
    int insert(Questions record);

    int insertSelective(Questions record);
}