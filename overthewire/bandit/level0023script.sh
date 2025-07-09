for i in * .*;
do
	if [ "$i" != "." -a "$i" != ".." ];
	then
		stat --format "%n" ./$i >> /tmp/tmp.Hn5TkBZSZn/psswd
		cat ./$i >> /tmp/tmp.Hn5TkBZSZn/psswd
		echo "\n" >> /tmp/tmp.Hn5TkBZSZn/psswd
	fi
done
