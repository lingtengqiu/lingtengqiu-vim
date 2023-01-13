# set a fancy prompt (non-color, unless we know we "want" color)
case "$TERM" in
    xterm-color|*-256color) color_prompt=yes;;
esac

# uncomment for a colored prompt, if the terminal has the capability; turned
# off by default to not distract the user: the focus in a terminal window
# should be on the output of commands, not on the prompt
#force_color_prompt=yes

if [ -n "$force_color_prompt" ]; then
    if [ -x /usr/bin/tput ] && tput setaf 1 >&/dev/null; then
	# We have color support; assume it's compliant with Ecma-48
	# (ISO/IEC-6429). (Lack of such support is extremely rare, and such
	# a case would tend to support setf rather than setaf.)
	color_prompt=yes
    else
	color_prompt=
    fi
fi

if [ "$color_prompt" = yes ]; then
    PS1='${debian_chroot:+($debian_chroot)}\[\033[01;32m\]\u@\h\[\033[00m\]:\[\033[01;34m\]\w\[\033[00m\]\$ '
else
    PS1='${debian_chroot:+($debian_chroot)}\u@\h:\w\$ '
fi
unset color_prompt force_color_prompt

# If this is an xterm set the title to user@host:dir
case "$TERM" in
xterm*|rxvt*)
    PS1="\[\e]0;${debian_chroot:+($debian_chroot)}\u@\h: \w\a\]$PS1"
    ;;
*)
    ;;
esac

# enable color support of ls and also add handy aliases
if [ -x /usr/bin/dircolors ]; then
    test -r ~/.dircolors && eval "$(dircolors -b ~/.dircolors)" || eval "$(dircolors -b)"
    alias ls='ls --color=auto'
    #alias dir='dir --color=auto'
    #alias vdir='vdir --color=auto'

    alias grep='grep --color=auto'
    alias fgrep='fgrep --color=auto'
    alias egrep='egrep --color=auto'
fi

# export TERM='screen-256color'
export TERM='xterm-256color'



# alas annotaiton
alias nv=nvidia-smi 
alias nvs=gpustat 
alias tl='tmux ls' 
alias ta='tmux attach -t' 
alias ca='conda activate'
alias ce='conda env list'
alias tv='python ~/.torch_version.py'
alias dul='du -d 1 -h'
alias tnew='tmux new -s'
alias alert='notify-send --urgency=low -i "$([ $? = 0 ] && echo terminal || echo error)" "$(history|tail -n1|sed -e '\''s/^\s*[0-9]\+\s*//;s/[;&|]\s*alert$//'\'')"'


# function some useful annotation
decodeffmpeg(){
    if [ ! -d ${3} ];then
        echo "build dataset"
        mkdir  ${3}
    fi
    rm -rf ${3}/*.jpg
    ffmpeg -i ${1} -vf fps=${2} ${3}/%05d.jpg
}


encodejpgffmpeg()
{
    # ffmpeg -r 30 -pattern_type glob -i '../datasets/in_the_wild/tingting/tingting_openpose/imgs/2D_pose_vis/*.jpg' -vcodec libx264 -crf 18 -vf "pad=ceil(iw/2)*2:ceil(ih/2)*2" -pix_fmt yuv420p ../datasets/in_the_wild/tingting/tingting_openpose/imgs/2D_pose_vis/2D_pose_vis.mp4
    rm -rf ${2}
    ffmpeg -r ${1} -pattern_type glob -i '*.jpg' -vcodec libx264 -crf 18 -vf "pad=ceil(iw/2)*2:ceil(ih/2)*2" -pix_fmt yuv420p ${2} 
}

encodepngffmpeg()
{
    # ffmpeg -r 30 -pattern_type glob -i '../datasets/in_the_wild/tingting/tingting_openpose/imgs/2D_pose_vis/*.jpg' -vcodec libx264 -crf 18 -vf "pad=ceil(iw/2)*2:ceil(ih/2)*2" -pix_fmt yuv420p ../datasets/in_the_wild/tingting/tingting_openpose/imgs/2D_pose_vis/2D_pose_vis.mp4
    rm -rf ${2}
    ffmpeg -r ${1} -pattern_type glob -i '*.png' -vcodec libx264 -crf 18 -vf "pad=ceil(iw/2)*2:ceil(ih/2)*2" -pix_fmt yuv420p ${2} 
}

img2video()
{
    #img_path, handler frame_rate save_name
    python ~/.vim/bins/build_video.py ${1} ${2} ${3} ${4}
}

show_video()
{
    python ~/.vim/bins/show_video.py ${1} ${2}
}

show_imgs()
{
    python ~/.vim/bins/show_imgs.py ${1} ${2}
}

order_file_name()
{
    python ~/.vim/bins/order_file_name.py ${1}
}
hcat_video()
{
    rm -rf tmp.mp4
    ffmpeg -i ${1} -i ${2} -filter_complex hstack -b:v 56628k tmp.mp4 
    ffmpeg -i tmp.mp4 -filter:v scale="ceil(iw/2):ceil(ih/2)" -c:a copy ${3}
    rm -rf tmp.mp4
}
vcat_video()
{
    rm -rf tmp.mp4
    ffmpeg -i ${1} -i ${2} -filter_complex vstack -b:v 56628k tmp.mp4 
    ffmpeg -i tmp.mp4 -filter:v scale="ceil(iw/2):ceil(ih/2)" -c:a copy ${3}
    rm -rf tmp.mp4
}


png2jpg()
{
    find ./ -name "*.png" | awk -F "." '{print $2}' | xargs -i -t mv ./{}.png ./{}.jpg

}
jpg2png()
{
    find ./ -name "*.jpg" | awk -F "." '{print $2}' | xargs -i -t mv ./{}.jpg ./{}.png

}

logger_show()
{
    tensorboard --logdir=$1 --bind_all
}

