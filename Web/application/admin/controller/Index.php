<?php
namespace app\admin\controller;

use think\Controller;
use think\Db;

class Index extends Controller
{
    public $res = [
        'code'=>200,
        'data_ssq'=>[],
        'data_dyj'=>[],
        'msg'=>''
    ];
    public function index(){
        if($this->request->isAjax()){
            $data_dyj = Db::name('lottery_phoenix_tree')->order('id','desc')->limit(1)->select();
            $data_ssq = Db::name('lottery_phoenix_tree_ssq')->order('id','open_time')->limit(1)->select();
//            json_decode($data_dyj[0]["content"]);
//            json_decode($data_ssq[0]);
            $this->res['code'] = '200';
            $this->res['data_ssq'] = $data_ssq[0];
            $this->res['data_dyj'] = $data_dyj[0]["content"];
            return $this->res;
        }
        return $this->fetch();
    }
}
