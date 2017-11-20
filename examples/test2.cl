class Cons{
	xcar : Int;
	xcdr : String;

    x : Int <-
        if 2<3
            then 2
        else 3
        fi
    xx : Int <- 10;

    isNil() : Bool { false };

	init(hd : Int, tl : String) : Cons {
		{
		xcar <- hd;
		xcdr <- tl;
		self;
		}
	};

};
