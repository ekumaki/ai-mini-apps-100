#!/usr/bin/env python3

import streamlit as st
import yaml
import subprocess
import sys
import os

def load_apps():
    with open('apps.yaml', 'r', encoding='utf-8') as f:
        return yaml.safe_load(f)

def filter_apps(apps, search_term, tag_filter):
    if not search_term and not tag_filter:
        return apps
    
    filtered = []
    for app in apps:
        match = True
        
        if search_term:
            search_lower = search_term.lower()
            match = match and (
                search_lower in app['name'].lower() or
                search_lower in app['description'].lower() or
                any(search_lower in tag.lower() for tag in app.get('tags', []))
            )
        
        if tag_filter and tag_filter != 'All':
            match = match and tag_filter in app.get('tags', [])
            
        if match:
            filtered.append(app)
    
    return filtered

def get_all_tags(apps):
    tags = set()
    for app in apps:
        tags.update(app.get('tags', []))
    return sorted(list(tags))

def run_app(command):
    try:
        result = subprocess.run(command, shell=True, capture_output=True, text=True, cwd=os.getcwd())
        if result.returncode == 0:
            st.success(f"コマンド実行成功: {command}")
            if result.stdout:
                st.code(result.stdout, language='text')
        else:
            st.error(f"コマンド実行エラー: {command}")
            if result.stderr:
                st.code(result.stderr, language='text')
    except Exception as e:
        st.error(f"実行中にエラーが発生しました: {str(e)}")

def main():
    st.set_page_config(
        page_title="100 Mini Apps Collection",
        page_icon="🎯",
        layout="wide"
    )
    
    # OGPメタタグの追加
    st.markdown("""
    <meta property="og:title" content="100 Mini Apps Collection - Python アプリコレクション" />
    <meta property="og:description" content="Python 3.12で構築された100個のミニアプリケーションのコレクション。計算機、税金計算、BMI計算など様々なツールを提供。" />
    <meta property="og:image" content="https://ekumaki.github.io/ai-mini-apps-100/static/ogp_image.png" />
    <meta property="og:url" content="https://ekumaki.github.io/ai-mini-apps-100/" />
    <meta property="og:type" content="website" />
    <meta property="og:site_name" content="100 Mini Apps Collection" />
    <meta name="twitter:card" content="summary_large_image" />
    <meta name="twitter:title" content="100 Mini Apps Collection - Python アプリコレクション" />
    <meta name="twitter:description" content="Python 3.12で構築された100個のミニアプリケーションのコレクション。計算機、税金計算、BMI計算など様々なツールを提供。" />
    <meta name="twitter:image" content="https://ekumaki.github.io/ai-mini-apps-100/static/ogp_image.png" />
    """, unsafe_allow_html=True)
    
    st.title("🎯 100 Mini Apps Collection")
    st.markdown("---")
    
    apps = load_apps()
    all_tags = get_all_tags(apps)
    
    # サイドバーでフィルタリング
    st.sidebar.header("🔍 検索 & フィルター")
    search_term = st.sidebar.text_input("🔎 キーワード検索", placeholder="アプリ名、説明、タグで検索...")
    tag_filter = st.sidebar.selectbox("🏷️ タグフィルター", ["All"] + all_tags)
    
    # ソート機能
    sort_by = st.sidebar.selectbox("📊 ソート", ["ID順", "名前順", "ステータス順"])
    
    filtered_apps = filter_apps(apps, search_term, tag_filter)
    
    if sort_by == "名前順":
        filtered_apps.sort(key=lambda x: x['name'])
    elif sort_by == "ステータス順":
        filtered_apps.sort(key=lambda x: x['status'])
    else:  # ID順
        filtered_apps.sort(key=lambda x: x['id'])
    
    st.sidebar.markdown("---")
    st.sidebar.markdown(f"📊 **統計情報**")
    st.sidebar.metric("総アプリ数", len(apps))
    st.sidebar.metric("表示中", len(filtered_apps))
    st.sidebar.metric("リリース済み", len([app for app in apps if app['status'] == 'release']))
    
    # メインコンテンツ
    if not filtered_apps:
        st.warning("条件に一致するアプリが見つかりませんでした。")
        return
    
    # 3列レイアウト
    cols = st.columns(3)
    
    for idx, app in enumerate(filtered_apps):
        col = cols[idx % 3]
        
        with col:
            # ステータスに応じたアイコン
            status_icon = "✅" if app['status'] == 'release' else "🚧"
            
            with st.container():
                st.markdown(f"### {status_icon} {app['name']}")
                st.markdown(f"**ID:** {app['id']:03d}")
                st.markdown(f"**説明:** {app['description']}")
                
                # タグ表示
                if app.get('tags'):
                    tag_str = " ".join([f"`{tag}`" for tag in app['tags']])
                    st.markdown(f"**タグ:** {tag_str}")
                
                # コマンド表示とコピー
                st.code(app['command'], language='bash')
                
                # ボタン行
                col1, col2 = st.columns(2)
                
                with col1:
                    if st.button(f"▶️ 実行", key=f"run_{app['id']}"):
                        with st.spinner(f"実行中: {app['name']}"):
                            run_app(app['command'])
                
                with col2:
                    if st.button(f"📋 コピー", key=f"copy_{app['id']}"):
                        # JavaScriptでクリップボードにコピー
                        st.write(f"```bash\n{app['command']}\n```")
                        st.success("コマンドをコピーしました！")
                
                st.markdown("---")
    
    # フッター
    st.markdown("---")
    st.markdown(
        """
        <div style='text-align: center; padding: 20px;'>
            <p>🚀 <strong>100 Mini Apps Collection</strong> - Python 3.12 Powered</p>
            <p>各アプリは独立して動作し、最小限の依存関係で構築されています。</p>
        </div>
        """,
        unsafe_allow_html=True
    )

if __name__ == "__main__":
    main()