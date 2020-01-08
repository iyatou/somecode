package com.yulanbo.bishe.mapper;

import com.yulanbo.bishe.model.StuLessionRate;
import org.apache.ibatis.annotations.Mapper;

@Mapper
public interface StuLessionRateMapper {
    int insert(StuLessionRate record);

    int insertSelective(StuLessionRate record);
}