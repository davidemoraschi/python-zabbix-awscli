set PROFILE_NAME=816247855850_AdministratorAccess
docker run -it -v "%USERPROFILE%\.aws":/home/glue_user/.aws -v "%cd%":/home/glue_user/workspace/ -e AWS_PROFILE=%PROFILE_NAME% -e DISABLE_SSL=true --rm -p 4343:4040 -p 18080:18080 --name glue_pyspark amazon/aws-glue-libs:glue_libs_3.0.0_image_01 pyspark