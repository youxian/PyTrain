 

# 在这里指定要处理的版本目录
shortVersion=5.16

# 这里还不能用${WORKSPACE}
echo ${shortVersion} > ${HOME}/Home/workspace/SymbolicateCrash_shortVersion

if [ ! -d "/Volumes/smb10.10.45.10/crash" ]; then
#[ -d FILE ] 如果 FILE 存在且是一个目录则为真。 crash目录不存在时
        mkdir -p /Volumes/smb10.10.45.10/
        mount_smbfs //root:xunlei@10.10.45.10/workgroup/ithunder_iOS_chenyiling /Volumes/smb10.10.45.10
fi
mkdir -p /Volumes/smb10.10.45.10/crash/${shortVersion}
cd /Volumes/smb10.10.45.10/crash/${shortVersion}/

# 避免无文件时直接返回通配字符串
shopt -s nullglob

for file in *.plist; do
        if [ ! -f "${file}_symbol.txt" ]; then
                exit 0
        fi
done

for file in *.crash; do
        if [ ! -f "${file}_symbol.txt" ]; then
                 exit 0
        fi
done

for file in *.ips; do
        if [ ! -f "${file}_symbol.txt" ]; then
                 exit 0
        fi
done

exit 1