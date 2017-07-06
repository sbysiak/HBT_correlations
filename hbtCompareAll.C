void hbtCompareAll(TString centrality){
    gROOT->ProcessLine(".L hbtCompare.C");
    gROOT->ProcessLine("hbtCompare(\"therm_atlas_comparision/fig_23a.root\", \""+centrality+"\")");
    gROOT->ProcessLine("hbtCompare(\"therm_atlas_comparision/fig_23b.root\", \""+centrality+"\")");
    gROOT->ProcessLine("hbtCompare(\"therm_atlas_comparision/fig_24a.root\", \""+centrality+"\")");
    gROOT->ProcessLine("hbtCompare(\"therm_atlas_comparision/fig_24b.root\", \""+centrality+"\")");
    gROOT->ProcessLine("hbtCompare(\"therm_atlas_comparision/fig_25a.root\", \""+centrality+"\")");
    gROOT->ProcessLine("hbtCompare(\"therm_atlas_comparision/fig_25b.root\", \""+centrality+"\")");
    gROOT->ProcessLine("hbtCompare(\"therm_atlas_comparision/fig_29a.root\", \""+centrality+"\")");
    gROOT->ProcessLine("hbtCompare(\"therm_atlas_comparision/fig_29b.root\", \""+centrality+"\")");
    //gROOT->ProcessLine("hbtCompare(\"therm_atlas_comparision/fig_30a.root\")");
    //gROOT->ProcessLine("hbtCompare(\"therm_atlas_comparision/fig_30b.root\")");
    gROOT->ProcessLine("hbtCompare(\"therm_atlas_comparision/fig_34a.root\", \""+centrality+"\")");
    gROOT->ProcessLine("hbtCompare(\"therm_atlas_comparision/fig_34_kt.root\", \""+centrality+"\")");
}
