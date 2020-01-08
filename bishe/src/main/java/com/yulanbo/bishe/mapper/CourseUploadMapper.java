package com.yulanbo.bishe.mapper;

import com.yulanbo.bishe.model.CourseUpload;
import org.apache.ibatis.annotations.Mapper;

@Mapper
public interface CourseUploadMapper {
    int insert(CourseUpload record);

    int insertSelective(CourseUpload record);
}