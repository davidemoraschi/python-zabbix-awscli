@echo off
set PROFILE_NAME=816247855850_AdministratorAccess
set JUPYTER_WORKSPACE_LOCATION="%cd%"
docker run -it ^
	-v "%USERPROFILE%\.ssh":/home/glue_user/.ssh ^
	-v %JUPYTER_WORKSPACE_LOCATION%:/home/glue_user/workspace/jupyter_workspace/ ^
	-v "%USERPROFILE%\.aws":/home/glue_user/.aws ^
	-v "%cd%":/home/glue_user/workspace/ ^
	-e AWS_PROFILE=%PROFILE_NAME% ^
	-e AWS_REGION=eu-west-1 ^
	-e DISABLE_SSL=true ^
	--rm -p 4040:4040 --rm -p 18080:18080 ^
	-p 8998:8998 -p 8888:8888 ^
	--name glue_jupyter_lab ^
	amazon/aws-glue-libs:glue_libs_4.0.0_image_01 ^
	/home/glue_user/jupyter/jupyter_start.sh
