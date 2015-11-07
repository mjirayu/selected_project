# -*- coding: utf-8 -*-
from django.shortcuts import render
from django.views.generic import TemplateView
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

from restaurant.models import RestaurantModel


class HomeView(TemplateView):
    template_name = "home.html"

    def get(self, request):
        return render(
            request,
            self.template_name,
        )


class SearchView(TemplateView):
    template_name = "search.html"

    def get(self, request):
        best_of_three = RestaurantModel.objects.all().order_by('-average')[:3]
        restaurants = RestaurantModel.objects.all().order_by('-average')[3:]
        categories = set(RestaurantModel.objects.values_list('category', flat=True))
        paginator = Paginator(restaurants, 6)

        page = request.GET.get('page')
        try:
            contacts = paginator.page(page)
        except PageNotAnInteger:
            # If page is not an integer, deliver first page.
            contacts = paginator.page(1)
        except EmptyPage:
            # If page is out of range (e.g. 9999), deliver last page of results.
            contacts = paginator.page(paginator.num_pages)

        return render(
            request,
            self.template_name,
            {
                'restaurants': contacts,
                'best_of_three': best_of_three,
                'categories': categories,
            },
        )


class SearchCategoryView(TemplateView):
    template_name = "search.html"

    def get(self, request, category):
        best_of_three = RestaurantModel.objects.filter(category=category).order_by('-average')[:3]
        restaurants = RestaurantModel.objects.filter(category=category).order_by('-average')[3:]
        categories = set(RestaurantModel.objects.values_list('category', flat=True))
        paginator = Paginator(restaurants, 6)

        page = request.GET.get('page')
        try:
            contacts = paginator.page(page)
        except PageNotAnInteger:
            # If page is not an integer, deliver first page.
            contacts = paginator.page(1)
        except EmptyPage:
            # If page is out of range (e.g. 9999), deliver last page of results.
            contacts = paginator.page(paginator.num_pages)

        return render(
            request,
            self.template_name,
            {
                'restaurants': contacts,
                'best_of_three': best_of_three,
                'categories': categories,
            },
        )
