class Main inherits IO {
    main() : SELF_TYPE {
    	{
            c <- (new Complex).init(1, 1);
    	    if
                c.reflect_X().reflect_Y() = c.reflect_0()
    	    then
                out_string("=)\n")
    	    else
                out_string("=(\n")
    	    fi;
    	}
    };
};

class Complex inherits IO {
    x : Int;
    y : Int;

    init(a : Int, b : Int) : Complex {
    	{
    	    x <- a;
    	    y <- b;
    	    self;
    	}
    };


    reflect_0() : Complex {
	{
	    x <- ~x;
	    y <- ~y;
	    self;
	}
    };

    reflect_X() : Complex {
	{
	    y <- ~y;
	    self;
	}
    };

    reflect_Y() : Complex {
	{
	    x <- ~x;
	    self;
	}
    };
};
