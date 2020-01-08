package com.yulanbo.bishe.mapper;

import com.yulanbo.bishe.model.VidioAddress;
import org.apache.ibatis.annotations.Mapper;

@Mapper
public interface VidioAddressMapper {
    int insert(VidioAddress record);

    int insertSelective(VidioAddress record);
}