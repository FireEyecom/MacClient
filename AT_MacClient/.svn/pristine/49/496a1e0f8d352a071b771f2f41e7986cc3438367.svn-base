ftp -n<<!
open 192.168.122.46
user anonymous 123456
prompt
cd /ci-jobs/AS/package/client/Mac_CN
lcd $WORKSPACE
get AnyShare_Mac-CN-LATEST.dmg
disconnect
bye
!


# function check(){  
#     local a="$1"  
#     printf "%d" "$a" &>/dev/null && echo "integer" && return  
#     printf "%d" "$(echo $a|sed 's/^[+-]\?0\+//')" &>/dev/null && echo "integer" && return  
#     printf "%f" "$a" &>/dev/null && echo "number" && return  
#     [ ${#a} -eq 1 ] && echo "char" && return  
#     echo "string"  
# }  
  
# echo $(check $isAnyshareProcssExist)  



isFUSEServiceProcssExist=`ps auxc | grep AnyShare | awk '{print $2}'`
if [ $isFUSEServiceProcssExist -ge 0 ];then
	kill -HUP $isFUSEServiceProcssExist
fi
isAnyshareProcssExist=`ps auxc | grep FUSEService | awk '{print $2}'`
if [ $isAnyshareProcssExist -ge 0 ];then
	kill -HUP $isAnyshareProcssExist
fi

rm -rf /Applications/AnyShare.app
open /Users/Elvis/desktop/AnyShare_Mac-CN-LATEST.dmg 
sleep 3
isDmgOpen=`df -h |grep /Volumes/AnyShare安装包|awk '{print $9}'`
until [ "$isDmgOpen" = "/Volumes/AnyShare安装包" ];do
	sleep 1
	isDmgOpen=`df -h |grep /Volumes/AnyShare安装包|awk '{print $9}'`
done
cp -rf /Volumes/AnyShare安装包/AnyShare.app /Applications
hdiutil detach /Volumes/AnyShare安装包


