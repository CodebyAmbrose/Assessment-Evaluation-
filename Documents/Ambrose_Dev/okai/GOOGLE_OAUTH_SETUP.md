# Google OAuth 配置说明

## 错误：redirect_uri_mismatch（重定向URI不匹配）

你看到的错误说明 Google Cloud Console 的 OAuth 凭据没有配置正确的授权 URI。

## 在 Google Cloud Console 中修复

1. 访问 [Google Cloud Console](https://console.cloud.google.com/)
2. 选择你的项目
3. 导航到：**APIs & Services**（API和服务）→ **Credentials**（凭据）
4. 点击你的 OAuth 2.0 Client ID

### 添加授权的 JavaScript 来源：
```
https://www.test.okai.uno
https://www.okai.uno
http://admin.test.okai.uno
```

### 添加授权的重定向 URI：
```
https://api.test.okai.uno/auth/google/callback
https://www.test.okai.uno
https://www.okai.uno
```

5. 点击 **保存**

## 所需的环境变量

### 后端 (okai-server/.env.production)：
```bash
PORT=3001
DB_HOST=localhost
DB_PORT=3306
DB_USERNAME=root
DB_PASSWORD=YOUR_PRODUCTION_DB_PASSWORD
DB_DATABASE=okai
JWT_SECRET=your-production-secret-change-me
FRONTEND_URL=https://www.test.okai.uno
BACKEND_URL=https://api.test.okai.uno

# Google OAuth - 从 @Ambrose 获取
GOOGLE_CLIENT_ID=
GOOGLE_CLIENT_SECRET=
NEXT_PUBLIC_GOOGLE_CLIENT_ID=
GOOGLE_REDIRECT_URI=https://api.test.okai.uno/auth/google/callback
NODE_ENV=production

# PayPal - 从 @Ambrose 获取
PAYPAL_ENV=live
PAYPAL_LIVE_CLIENT_ID=
PAYPAL_LIVE_CLIENT_SECRET=
PAYPAL_LIVE_WEBHOOK_ID=
PAYPAL_LIVE_EMAIL=
PAYPAL_LIVE_MONTHLY_PLAN_ID=
PAYPAL_LIVE_YEARLY_PLAN_ID=
```

### 前端 (okai-web/.env.production)：
```bash
NEXT_PUBLIC_BACKEND_URL=https://api.test.okai.uno
FRONTEND_URL=https://www.test.okai.uno

# Google OAuth - 从 @Ambrose 获取
NEXT_PUBLIC_GOOGLE_CLIENT_ID=

# PayPal - 从 @Ambrose 获取
NEXT_PUBLIC_PAYPAL_ENV=live
NEXT_PUBLIC_PAYPAL_MONTHLY_PLAN_ID=
NEXT_PUBLIC_PAYPAL_YEARLY_PLAN_ID=
```

## PayPal 配置

### 后端：
- 使用 **LIVE**（生产）模式
- 月度计划：P-24H646629F660614UNGRQIOA
- 年度计划：P-02X716921D238231PNGRQJ4Y

### 前端：
- 使用 **LIVE**（生产）模式
- 相同的计划 ID

## 部署后测试

1. 在 https://www.test.okai.uno/login 测试 Google 登录
2. 在 https://www.test.okai.uno/upgrade 测试 PayPal 订阅
3. 监控日志查看是否有错误

## 注意事项

- 记得在服务器上的生产环境 .env 文件中更新 `DB_PASSWORD` 和 `JWT_SECRET`
- 数据库应该使用这个 SQL 创建：`c:\Users\OMEN\Downloads\0314.sql`
- 服务器 IP：47.85.177.225（或根据当前 deploy.sh 使用 103.100.159.44）
