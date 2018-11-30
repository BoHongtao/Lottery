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
        return $this->fetch();
    }
    public function data(){
        if($this->request->isAjax()){
            $fn = $this->request->get('callback');
            $data_dyj = Db::name('lottery_phoenix_tree')->order('id','desc')->limit(1)->select();
            $data_ssq = Db::name('lottery_phoenix_tree_ssq')->order('id','open_time')->limit(1)->select();
            $this->res['code'] = '200';
            $this->res['data_ssq'] = $data_ssq[0];
            $this->res['data_dyj'] = $data_dyj[0]["content"];
            $arr = json_encode($this->res);
            return $fn."($arr)";
        }
    }
}
