class Cons{
	xcar : Int;
	xcdr : String;

	isNil() : Bool { false };

	init(hd : Int, tl : String) : Cons {
		{
		xcar <- hd;
		xcdr <- tl;
		self;
		}
	};
	xx : Int <- 10;
};
