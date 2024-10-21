# NoSQL Databases

NoSQL is an approach to databases that represents a shift away from traditional relational database management systems (RDBMS). It is particularly useful for storing **unstructured data**, which is growing far more rapidly than structured data and does not fit the relational schemas of RDBMS. Examples include:  
- User and session data  
- Chat, messaging, and log data  
- Time series data, such as IoT and device data  
- Large objects, such as videos and images  

---

## Types of NoSQL Databases

NoSQL databases fall into four main categories:

### 1. **Key-Value Data Stores**  
Key-value NoSQL databases emphasize simplicity and are useful for accelerating an application by supporting high-speed **read and write processing** of non-transactional data.  
- Stored values can be any type of binary object (e.g., text, video, or JSON documents).  
- Data is accessed via a key.  

### 2. **Document Stores**  
Document databases typically store **self-describing JSON, XML, or BSON documents**.  
- Similar to key-value stores, but here the value is a **document** that stores all data related to a specific key.  
- Popular fields in the document can be **indexed** to enable fast retrieval without knowing the key.  
- Each document can have the same or a different structure.

### 3. **Wide-Column Stores**  
Wide-column NoSQL databases store data in **tables with rows and columns**, similar to RDBMS, but:
- The **names and formats of columns** can vary from row to row across the table.  
- Columns of related data are grouped together, enabling a query to **retrieve related data in a single operation**.  
- In RDBMS, related data would be stored in separate rows in different places on disk, requiring **multiple disk operations** for retrieval.

### 4. **Graph Stores**  
Graph stores use **graph structures** to store, map, and query relationships.  
- They provide **index-free adjacency**, meaning adjacent elements are **linked directly** without using an index.  
- This structure makes graph stores ideal for applications involving complex relationships, such as social networks and recommendation engines.

---

**Multi-modal databases** leverages some conbination of the four types described above and therefore can support a sider range of applications.
---
