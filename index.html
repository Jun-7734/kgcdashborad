import React, { useState } from 'react';
import { 
  BarChart, Bar, XAxis, YAxis, CartesianGrid, Tooltip, Legend, ResponsiveContainer, 
  LineChart, Line, PieChart, Pie, Cell, AreaChart, Area 
} from 'recharts';
import { 
  TrendingUp, Users, MessageCircle, AlertTriangle, 
  MapPin, ShoppingCart, Activity, Gift 
} from 'lucide-react';

const App = () => {
  // Mock Data: Sales Performance
  const salesData = [
    { name: 'Monday', 수도권: 4000, 지방: 2400 },
    { name: 'Tuesday', 수도권: 4500, 지방: 2300 },
    { name: 'Wednesday', 수도권: 5200, 지방: 2200 },
    { name: 'Thursday', 수도권: 6100, 지방: 2100 },
    { name: 'Friday', 수도권: 7500, 지방: 2000 },
    { name: 'Saturday', 수도권: 8200, 지방: 2500 },
    { name: 'Sunday', 수도권: 7800, 지방: 2600 },
  ];

  // Mock Data: Age Distribution
  const ageData = [
    { name: '2030 사회초년생', value: 45 },
    { name: '40대 직장인', value: 25 },
    { name: '50대 이상', value: 20 },
    { name: '기타', value: 10 },
  ];

  // Mock Data: Keyword Growth
  const keywordData = [
    { month: '2월', 등산: 100, 테니스: 80 },
    { month: '3월 1주', 등산: 110, 테니스: 95 },
    { month: '3월 2주', 등산: 130, 테니스: 120 },
    { month: '3월 3주', 등산: 160, 테니스: 150 },
    { month: '3월 4주', 등산: 210, 테니스: 195 },
  ];

  const COLORS = ['#ef4444', '#f87171', '#fca5a5', '#fee2e2'];

  return (
    <div className="min-h-screen bg-gray-50 p-4 md:p-8 font-sans">
      {/* Header */}
      <header className="mb-8 flex flex-col md:flex-row justify-between items-start md:items-center gap-4">
        <div>
          <h1 className="text-2xl font-bold text-gray-900">에브리타임 밸런스 마케팅 대시보드</h1>
          <p className="text-gray-500 text-sm">2026년 3월 4주차 전략 리포트 시각화</p>
        </div>
        <div className="flex gap-2">
          <span className="px-3 py-1 bg-red-100 text-red-700 rounded-full text-xs font-semibold">리뉴얼 제품군</span>
          <span className="px-3 py-1 bg-blue-100 text-blue-700 rounded-full text-xs font-semibold">전략 보고용</span>
        </div>
      </header>

      {/* Quick Stats */}
      <div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-4 gap-4 mb-8">
        {[
          { title: '수도권 판매 성장', value: '+15%', icon: TrendingUp, color: 'text-green-600', bg: 'bg-green-50' },
          { title: '핵심 타겟 비중', value: '45%', icon: Users, color: 'text-blue-600', bg: 'bg-blue-50' },
          { title: '액티브 키워드 증가', value: '+30%', icon: Activity, color: 'text-purple-600', bg: 'bg-purple-50' },
          { title: '지방 판매 추이', value: '-2%', icon: AlertTriangle, color: 'text-red-600', bg: 'bg-red-50' },
        ].map((stat, idx) => (
          <div key={idx} className="bg-white p-6 rounded-2xl shadow-sm border border-gray-100">
            <div className="flex justify-between items-start">
              <div>
                <p className="text-sm text-gray-500 mb-1">{stat.title}</p>
                <h3 className={`text-2xl font-bold ${stat.color}`}>{stat.value}</h3>
              </div>
              <div className={`${stat.bg} p-2 rounded-lg`}>
                <stat.icon size={20} className={stat.color} />
              </div>
            </div>
          </div>
        ))}
      </div>

      {/* Main Charts */}
      <div className="grid grid-cols-1 lg:grid-cols-2 gap-8 mb-8">
        {/* Sales Trend Chart */}
        <div className="bg-white p-6 rounded-2xl shadow-sm border border-gray-100">
          <h3 className="text-lg font-bold mb-4 flex items-center gap-2">
            <MapPin size={18} className="text-red-600" /> 수도권 vs 지방 판매 추이 (채널별)
          </h3>
          <div className="h-[300px]">
            <ResponsiveContainer width="100%" height="100%">
              <BarChart data={salesData}>
                <CartesianGrid strokeDasharray="3 3" vertical={false} />
                <XAxis dataKey="name" />
                <YAxis />
                <Tooltip cursor={{fill: '#f3f4f6'}} />
                <Legend />
                <Bar dataKey="수도권" fill="#ef4444" radius={[4, 4, 0, 0]} />
                <Bar dataKey="지방" fill="#9ca3af" radius={[4, 4, 0, 0]} />
              </BarChart>
            </ResponsiveContainer>
          </div>
          <p className="text-xs text-gray-400 mt-4 text-center">* 수도권: 편의점 채널 강세 / 지방: 대형마트 정체</p>
        </div>

        {/* Keyword Growth Chart */}
        <div className="bg-white p-6 rounded-2xl shadow-sm border border-gray-100">
          <h3 className="text-lg font-bold mb-4 flex items-center gap-2">
            <Activity size={18} className="text-orange-600" /> 라이프스타일 키워드 언급 추이
          </h3>
          <div className="h-[300px]">
            <ResponsiveContainer width="100%" height="100%">
              <AreaChart data={keywordData}>
                <defs>
                  <linearGradient id="colorHiking" x1="0" y1="0" x2="0" y2="1">
                    <stop offset="5%" stopColor="#f97316" stopOpacity={0.8}/>
                    <stop offset="95%" stopColor="#f97316" stopOpacity={0}/>
                  </linearGradient>
                </defs>
                <XAxis dataKey="month" />
                <YAxis />
                <CartesianGrid strokeDasharray="3 3" vertical={false} />
                <Tooltip />
                <Area type="monotone" dataKey="등산" stroke="#f97316" fillOpacity={1} fill="url(#colorHiking)" />
                <Area type="monotone" dataKey="테니스" stroke="#0ea5e9" fillOpacity={0.1} fill="#0ea5e9" />
                <Legend />
              </AreaChart>
            </ResponsiveContainer>
          </div>
        </div>
      </div>

      <div className="grid grid-cols-1 lg:grid-cols-3 gap-8">
        {/* Customer Segment */}
        <div className="bg-white p-6 rounded-2xl shadow-sm border border-gray-100">
          <h3 className="text-lg font-bold mb-4">구매 고객 구성 (연령)</h3>
          <div className="h-[250px]">
            <ResponsiveContainer width="100%" height="100%">
              <PieChart>
                <Pie
                  data={ageData}
                  cx="50%"
                  cy="50%"
                  innerRadius={60}
                  outerRadius={80}
                  paddingAngle={5}
                  dataKey="value"
                >
                  {ageData.map((entry, index) => (
                    <Cell key={`cell-${index}`} fill={COLORS[index % COLORS.length]} />
                  ))}
                </Pie>
                <Tooltip />
                <Legend verticalAlign="bottom" />
              </PieChart>
            </ResponsiveContainer>
          </div>
        </div>

        {/* Action Strategy Card */}
        <div className="lg:col-span-2 bg-white p-6 rounded-2xl shadow-sm border border-gray-100">
          <h3 className="text-lg font-bold mb-6">전략적 핵심 액션 아이템</h3>
          <div className="space-y-4">
            <div className="flex items-start gap-4 p-4 bg-gray-50 rounded-xl">
              <div className="bg-red-500 p-2 rounded-full text-white">
                <Gift size={16} />
              </div>
              <div>
                <h4 className="font-semibold text-gray-900 text-sm">편의점 채널 프로모션 최적화</h4>
                <p className="text-xs text-gray-500 mt-1">사회초년생의 반복 구매 습관 형성을 위한 2+1 및 모바일 바우처 증정</p>
              </div>
            </div>
            <div className="flex items-start gap-4 p-4 bg-gray-50 rounded-xl">
              <div className="bg-orange-500 p-2 rounded-full text-white">
                <Activity size={16} />
              </div>
              <div>
                <h4 className="font-semibold text-gray-900 text-sm">'Active Lifestyle' 캠페인 가동</h4>
                <p className="text-xs text-gray-500 mt-1">#오운완 테니스/등산 커뮤니티 타겟 SNS 챌린지 및 인플루언서 협업</p>
              </div>
            </div>
            <div className="flex items-start gap-4 p-4 bg-gray-50 rounded-xl">
              <div className="bg-blue-500 p-2 rounded-full text-white">
                <MessageCircle size={16} />
              </div>
              <div>
                <h4 className="font-semibold text-gray-900 text-sm">패키지 QC 강화 및 가격 심리 방어</h4>
                <p className="text-xs text-gray-500 mt-1">개봉 편의성 개선 및 대형마트용 실속형 대용량 패키지 기획</p>
              </div>
            </div>
          </div>
        </div>
      </div>

      {/* Footer / Insights */}
      <div className="mt-8 p-6 bg-red-900 text-white rounded-2xl">
        <h4 className="text-lg font-bold mb-2 flex items-center gap-2">
          <TrendingUp size={20} /> 팀장 Insight 요약
        </h4>
        <p className="text-red-100 text-sm opacity-90 leading-relaxed">
          "리뉴얼 제품이 2030의 라이프스타일(편의점, 아웃도어 스포츠)에 성공적으로 침투하고 있습니다. 
          이제는 브랜드 포지셔닝을 '전통적 보양'에서 '능동적 퍼포먼스 서포터'로 전환하는 마케팅 캠페인에 집중할 때입니다."
        </p>
      </div>
    </div>
  );
};

export default App;
