/*
A KBase module: TestServiceCalls
*/

module TestServiceCalls {
    /*
        Insert your typespec information here.
    */

    typedef structure {
        string ref;
    } Params;

    typedef structure {

    } Output;

    funcdef get_feature_ids(Params p) returns (Output o) authentication required;
};
