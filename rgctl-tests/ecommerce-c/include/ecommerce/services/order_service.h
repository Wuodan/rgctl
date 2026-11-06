#ifndef EC_ORDER_SERVICE_H
#define EC_ORDER_SERVICE_H
#include "ecommerce/types.h"
#include <sqlite3.h>
int order_checkout(sqlite3 *db, int user_id);
int order_get(sqlite3 *db, int id, void *out);
int order_list_for_user(sqlite3 *db, int *count);
int order_to_dto(const void *entity, char *buf, size_t len);
#endif
