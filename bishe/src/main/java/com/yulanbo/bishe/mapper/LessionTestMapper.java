package com.yulanbo.bishe.mapper;

import com.yulanbo.bishe.model.LessionTest;
import org.apache.ibatis.annotations.Mapper;

@Mapper
public interface LessionTestMapper {
    int insert(LessionTest record);

    int insertSelective(LessionTest record);
}