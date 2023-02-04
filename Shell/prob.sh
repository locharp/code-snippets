# !/bin/dash

factorial ()
{
    res=1
    local i=2

    while [ $i -le $1 ]
    do
        res=$(( res * i ))
        i=$(( i + 1 ))
    done
}

nPr ()
{
    factorial $1
    local n=$res
    factorial $(( $1 - $2 ))
    local r=$res
    res=$(( n / r ))
}

nCr ()
{
    nPr $1 $2
    local n=$res
    factorial $2
    local r=$res
    res=$(( n / r ))
}

exact ()
{
    nCr $1 $2
    local c=$res
    res=$( echo $1 $2 $3 $c | awk '{ printf "%f", ($3**$2) * ((1.0-$3)**($1-$2)) * $4}' )
}

at_least ()
{
    if [ $2 -gt $(( $1 / 2 )) ]
    then
        local total=0
        local i=$2
        while [ $i -le $1 ]
        do
            exact $1 $i $3
            total=$( echo $total $res | awk '{ printf "%f", $1+$2 }' )
            i=$(( i + 1 ))
        done
    else
        local total=1
        local i=0
        while [ $i -lt $2 ]
        do        
            exact $1 $i $3
            total=$( echo $total $res | awk '{ printf "%f", $1-$2 }' )
            i=$(( i + 1 ))
        done
    fi
    res=$total
}

at_most ()
{
    at_least $1 $(( $2 + 1 )) $3
    res=$( echo $res | awk '{ printf "%f", 1-$1 }' )
}

a_or_b ()
{
    res=$(( $1 + $2 - $3 ))
    echo $res/$4
    res=$( echo $res $4 | awk '{ printf "%f", $1 / $2 }' )
}

case  "$1" in
    'factorial' )
        factorial $2
        ;;
    'nPr' )
        nPr $2 $3
        ;;
    'nCr' )
        nCr $2 $3
        ;;
    'exact' )
        exact $2 $3 $4
        ;;
    'at_least' )
        at_least $2 $3 $4
        ;;
    'at_most' )
        at_most $2 $3 $4
        ;;
    'a_or_b' )
        a_or_b $2 $3 $4 $5
        ;;
esac

echo $res