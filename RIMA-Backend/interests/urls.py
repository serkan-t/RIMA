from django.urls import path

from . import views

urlpatterns = [
    path('trigger-paper-updata/', views.TriggerPaperUpdate.as_view()),
    path('trigger-data-updata/', views.TriggerDataUpdate.as_view()),
    path('long-term/', views.LongTermInterestView.as_view()),
    path('long-term/<int:pk>/', views.LongTermInterestItemView.as_view()),
#     path('recommended-publications', views.recommended_publications), #LK
    path('recommended-publications', views.RecommendedPublications.as_view()),
    path('papers/', views.PaperView.as_view()),
    path('papers/<int:pk>/', views.PaperItemView.as_view()),
    path('similarity/<int:pk>/', views.SimilarityView.as_view()),
    path(
        'black-listed-keywords/<int:pk>/',
        views.UserBlacklistedKeywordItemView.as_view(),
    ),
    path('interest-extraction/', views.PublicInterestExtractionView.as_view()),
    path('similarity/', views.PublicKeywordSimilarityView.as_view()),
    path('interest-extraction/wiki-categories/',
         views.PublicKeywordCategoriesView.as_view()),
    path('short-term/user/<int:pk>/',
         views.UserShortTermInterestView.as_view()),
    path('long-term/user/<int:pk>/', views.UserLongTermInterestView.as_view()),
    #to be removed
    path('long/', views.UserShortTermInterestViewDummy.as_view()),
    path('activity-stats/user/<int:pk>/',
         views.UserActivityStatsView.as_view()),
    path('stream-graph/user/<int:pk>/', views.UserStreamGraphView.as_view()),
    path('recommended-tweets', views.recommended_tweets),
    path('tweets', views.TweetView.as_view()),
    path("tweets/<slug:id_str>", views.DeleteTweetView.as_view()),
    path("hello", views.HelloView.as_view()),
    path('laktopics/<pk1>/<pk2>', views.TopicsView.as_view()),
    path('lakkeywords/<pk1>/<pk2>', views.KeywordsView.as_view()),
    path('alltopics/', views.AllTopicsViewDB.as_view()),
    path('topkeywords/<pk>', views.TopicBarView.as_view()),
    path('toptopics/<pk>', views.TopicBarViewTopics.as_view()),
    path('populatetopics/<pk>', views.populateTopicView.as_view()),
    path('populatekeys/<pk>', views.populateKeyView.as_view()),
    path('topicdetails/<pk1>/<pk2>', views.getTopicBarValues.as_view()),
    path('keydetails/<pk1>/<pk2>', views.getKeyBarValues.as_view()),
    path('comparetopics/', views.vennPlotView.as_view()),
    path('getalltopicsresults/', views.allTopics.as_view()),
    path('getallkeysresults/', views.allKeys.as_view()),
    path('gettopicsyearwise/<pk>', views.AllTopicDicts.as_view()),
    path('gettopicsforpie/<pk1>/<pk2>', views.TopicPieView.as_view()),
    path('getkeysforpie/<pk1>/<pk2>', views.KeyPieView.as_view()),
    path('getalltopicsevolution/', views.MultipleTopicAreaView.as_view()),
    path('getallkeysevolution/', views.MultipleKeyAreaView.as_view()),
    path('fetchpaper/', views.FetchPaperView.as_view()),
    path('fetchallauthors/', views.AuthorsFetchView.as_view()),
    path('fetchallauthorsdict/', views.AuthorsDictFetchView.as_view()),
    path('topicoverview/', views.TopicOverview.as_view()),
    path('commontopics/<pk1>/<pk2>', views.VennOverview.as_view()),
    path('commonkeys/<pk1>/<pk2>', views.VennOverviewKeys.as_view()),
    path('getallkeywords/<pk>', views.AllKeywordsView.as_view()),
    path('getalltopics/<pk>', views.AllTopicsView.as_view()),
    path('getalltitles/<pk1>/<pk2>', views.SearchKeywordView.as_view()),
    path('searchtopic/<pk1>/<pk2>', views.SearchTopicView.as_view()),
    path('getalltopiclist/', views.FetchTopicView.as_view()),
    path('getallkeylist/', views.FetchKeyView.as_view()),
    path('getallauthorslist/<pk1>/<pk2>/<pk3>',
         views.FetchAuthorView.as_view()),
    path('getallauthorsdict/', views.FetchAuthorsDict.as_view()),
    path('getauthorsyearlist/<pk>', views.AuthorFetchYearView.as_view()),
    path('getoverviewtopicdetails/<pk1>/<pk2>',
         views.OverviewChartViewTopics.as_view()),
    path('getoverviewkeydetails/<pk1>/<pk2>',
         views.OverviewChartViewKeywords.as_view()),
    path('getabstractdetails/<pk1>/<pk2>', views.FetchAbstractView.as_view()),
    path('getauthortopicdetails/', views.AuthorTopicComparisonView.as_view()),
    #path('getauthorkeydetails/',views.AuthorKeywordComparisonView.as_view()),
    path('getauthorvsconfdetails/<pk1>/<pk2>',
         views.CompareAuthorConf.as_view()),
    path('insertauthordb/', views.AuthorDBInsertView.as_view()),
    path('authorcomparison/<pk1>/<pk2>', views.AuthorComparisonData.as_view()),
    path('authorconfcomparison/<pk1>/<pk2>/<pk3>',
         views.AuthorConfComparisionView.as_view()),
    path('updatealltopics/', views.UpdateAllTopics.as_view()),
    #added by mouadh
    path('getsimilarity/', views.similartweets.as_view()),
    #for demo
    #path('updateprinttext/',views.printHelloBackend.as_view())
     #Jaleh
#     path('recommended-papers', views.recommended_papers),
    path('recommended-interests-similarities', views.recommended_interests_similarities),
    path('recommended-keyword-similarities', views.recommended_keywords_similarities),
]
