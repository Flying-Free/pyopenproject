import business.service_factory as service_factory


class WorkPackage:

    def __init__(self, json_obj):
        self.__dict__ = json_obj

    def get_attachments(self):
        if self._links.attachments.href is not None:
            return service_factory.ServiceFactory.get_attachment_service()\
                .find_by_context(self._links.attachments.href)
        return None

    # TODO:
    #     "addAttachment": {
    #       "href": "/api/v3/work_packages/147/attachments",
    #       "method": "post"
    #     },
    #     "update": {
    #       "href": "/api/v3/work_packages/147/form",
    #       "method": "post"
    #     }

    def get_schema(self):
        if self._links.schema.href is not None:
            return service_factory.ServiceFactory.get_schema_service()\
                .find_by_context(self._links.schema.href)
        return None

    def delete(self):
        service_factory.ServiceFactory.get_work_package_service()\
            .delete(self.id)

    # TODO:
    #     "updateImmediately": {
    #       "href": "/api/v3/work_packages/147",
    #       "method": "patch"
    #     },
    #     "logTime": {
    #       "href": "/work_packages/147/time_entries/new",
    #       "type": "text/html",
    #       "title": "Log time on ZOR-DE-0326287 // UAT // Z-Workflow // Deployment"
    #     },
    #     "move": {
    #       "href": "/work_packages/147/move/new",
    #       "type": "text/html",
    #       "title": "Move ZOR-DE-0326287 // UAT // Z-Workflow // Deployment"
    #     },
    #     "copy": {
    #       "href": "/work_packages/147/copy",
    #       "title": "Copy ZOR-DE-0326287 // UAT // Z-Workflow // Deployment"
    #     }

    def get_pdf(self):
        if self._links.pdf.href is not None:
            return service_factory.ServiceFactory.get_work_package_service()\
                .download_pdf(self._links.pdf.href)
        return None

    def get_atom(self):
        if self._links.pdf.href is not None:
            return service_factory.ServiceFactory.get_work_package_service()\
                .download_atom(self._links.pdf.href)
        return None

    def get_available_relation_candidates(self):
        if self._links.availableRelationCandidates.href is not None:
            return service_factory.ServiceFactory.get_work_package_service()\
                .find_by_context(self._links.availableRelationCandidates.href)
        return None

    def get_custom_fields(self):
        if self._links.customFields.href is not None:
            return service_factory.ServiceFactory.get_custom_object_service()\
                .find_by_context(self._links.customFields.href)
        return None

    # TODO:
    #   "configureForm": {
    #     "href": "/types/1/edit?tab=form_configuration",
    #     "type": "text/html",
    #     "title": "Configure form"
    #   }

    def get_activities(self):
        if self._links.activities.href is not None:
            return service_factory.ServiceFactory.get_activity_service()\
                .find_by_contrext(self._links.activities.href)
        return None

    def get_available_watchers(self):
        if self._links.availableWatchers.href is not None:
            return service_factory.ServiceFactory.get_work_package_service()\
                .find_by_context(self._links.availableWatchers.href)
        return None

    def get_watchers(self):
        if self._links.watchers.href is not None:
            return service_factory.ServiceFactory.get_work_package_service()\
                .find_by_context(self._links.watchers.href)
        return None

    def get_relations(self):
        if self._links.relations.href is not None:
            return service_factory.ServiceFactory.get_relation_service()\
                .find_by_context(self._links.relations.href)
        return None

    def get_revisions(self):
        if self._links.revisions.href is not None:
            return service_factory.ServiceFactory.get_revision_service()\
                .find_by_context(self._links.revisions.href)
        return None

    # TODO:
    #   "addWatcher": {
    #     "href": "/api/v3/work_packages/147/watchers",
    #     "method": "post",
    #     "payload": {
    #       "user": {
    #         "href": "/api/v3/users/{user_id}"
    #       }
    #     },
    #     "templated": true
    #   },
    #   "removeWatcher": {
    #     "href": "/api/v3/work_packages/147/watchers/{user_id}",
    #     "method": "delete",
    #     "templated": true
    #   },
    #   "addRelation": {
    #     "href": "/api/v3/work_packages/147/relations",
    #     "method": "post",
    #     "title": "Add relation"
    #   },
    #   "addChild": {
    #     "href": "/api/v3/projects/zurich-baseline-de/work_packages",
    #     "method": "post",
    #     "title": "Add child of ZOR-DE-0326287 // UAT // Z-Workflow // Deployment"
    #   },
    #   "changeParent": {
    #     "href": "/api/v3/work_packages/147",
    #     "method": "patch",
    #     "title": "Change parent of ZOR-DE-0326287 // UAT // Z-Workflow // Deployment"
    #   },
    #   "addComment": {
    #     "href": "/api/v3/work_packages/147/activities",
    #     "method": "post",
    #     "title": "Add comment"
    #   },
    #   "previewMarkup": {
    #     "href": "/api/v3/previewing/markdown?context=/api/v3/work_packages/147",
    #     "method": "post"
    #   },

    def get_time_entries(self):
        if self._links.timeEntries.href is not None:
            return service_factory.ServiceFactory.get_time_entry_service()\
                .find_by_context(self._links.timeEntries.href)
        return None

    def get_category(self):
        if self._links.category.href is not None:
            return service_factory.ServiceFactory.get_category_service()\
                .find_by_context(self._links.category.href)
        return None

    def get_type(self):
        if self._links.types.href is not None:
            return service_factory.ServiceFactory.get_type_service()\
                .find_by_context(self._links.types.href)
        return None

    def get_priority(self):
        if self._links.priority.href is not None:
            return service_factory.ServiceFactory.get_priority_service()\
                .find_by_context(self._links.priority.href)
        return None

    def get_project(self):
        if self._links.project.href is not None:
            return service_factory.ServiceFactory.get_project_service()\
                .find_by_context(self._links.project.href)
        return None

    def get_status(self):
        if self._links.status.href is not None:
            return service_factory.ServiceFactory.get_status_service()\
                .find_by_context(self._links.status.href)
        return None

    def get_author(self):
        if self._links.author.href is not None:
            return service_factory.ServiceFactory.get_user_service()\
                .find_by_context(self._links.author.href)
        return None

    def get_responsible(self):
        if self._links.responsible.href is not None:
            return service_factory.ServiceFactory.get_group_service()\
                .find_by_context(self._links.responsible.href)
        return None

    def get_assignee(self):
        if self._links.assignee.href is not None:
            return service_factory.ServiceFactory.get_user_service()\
                .find_by_context(self._links.assignee.href)
        return None

    def get_version(self):
        if self._links.version.href is not None:
            return service_factory.ServiceFactory.get_version_service()\
                .find_by_context(self._links.version.href)
        return None

    # TODO:
    #   "logCosts": {
    #     "href": "/work_packages/147/cost_entries/new",
    #     "type": "text/html",
    #     "title": "Log costs on ZOR-DE-0326287 // UAT // Z-Workflow // Deployment"
    #   },
    #   "showCosts": {
    #     "href": "/work_packages/147/cost_entries",
    #     "type": "text/html",
    #     "title": "Show cost entries"
    #   }

    def get_custom_object(self):
        if self._links.costObject.href is not None:
            return service_factory.ServiceFactory.get_custom_object_service()\
                .find_by_context(self._links.costObject.href)
        return None

    def get_cost_by_type(self):
        if self._links.costsByType.href is not None:
            return service_factory.ServiceFactory.get_work_package_service()\
                .find_by_context(self._links.costsByType.href)
        return None

    # TODO:
    #   "customField4": {
    #     "title": "Request",
    #     "href": "/api/v3/custom_options/3"
    #   },
    #   "watch": {
    #     "href": "/api/v3/work_packages/147/watchers",
    #     "method": "post",
    #     "payload": {
    #       "user": {
    #         "href": "/api/v3/users/13"
    #       }
    #     }
    #   }

    def get_parent(self):
        if self._links.parent.href is not None:
            service_factory.ServiceFactory.get_work_package_service()\
                .find_by_context(self._links.parent.href)
        return None

    def get_ancestors(self):
        if not self._links.ancestors:
            return None
        else:
            for ancestor in self._links.ancestors:
                yield service_factory.ServiceFactory.get_work_package_service()\
                    .find_by_context(ancestor.href)

    def get_custom_actions(self):
        if not self._links.customActions:
            return None
        else:
            for custom_action in self._links.customActions:
                yield service_factory.ServiceFactory.get_custom_action_service()\
                    .find_by_context(custom_action.href)

    def __str__(self):
        return self.__dict__
